import os
import argparse
import pandas as pd

from bootcamps.sheet_connector import SheetConnector
from bootcamps.bl.dbsetup import DBConnector
from bootcamps.config import CONFIG


class DBLoader:

    def load_registration_sheet_to_table(self):
        conn = SheetConnector()
        df = conn.load_sheet(CONFIG.registration.file_id, CONFIG.registration.sheet_id)
        #df = pd.read_csv("test.csv")
        df = df.iloc[: , : len(CONFIG.registration.columns)]
        df.columns = CONFIG.registration.columns

        s=  df['bootcamps'].str.split(',').apply(pd.Series, 1).stack()
        s = s.str.strip(" ")
        s.index = s.index.droplevel(-1)
        s.name = 'bootcamps'
        del df["bootcamps"]
        df = df.join(s)

        dbc = DBConnector()
        bootcamps = pd.read_sql_table(CONFIG.bootcamps.table_id, con=dbc.engine)
        df["bootcamp_id"] = df["bootcamps"].apply(lambda b_name: bootcamps[bootcamps["identifying_str"].apply(lambda str : b_name.lower().find(str) > -1)]["bootcamp_id"].values[0])
        # duplicates are ignored therefore this sets to 0 only new records
        df["is_processed"] = 0
        df["course_completed"] = 0
        df["cert_sent"] = 0
        self.load_df_to_table(df , CONFIG.registration.table_id)

    def load_grades_to_table(self):
        dbc = DBConnector()
        bootcamps = pd.read_sql_table(CONFIG.bootcamps.table_id, con=dbc.engine)

        for file in os.listdir(CONFIG.csv_dump_path):
            df = pd.read_csv(os.path.join(CONFIG.csv_dump_path , file))
            df = df.melt(id_vars=["Student","ID",	"SIS User ID",	"SIS Login ID",	"Section"] , var_name="assignment" , value_name="score")
            df.columns = CONFIG.grades.columns
            #df["section"] = df["section"].str.replace("Training - " , "")
            id = bootcamps[bootcamps["identifying_str"].apply(lambda str : file.lower().replace("_" , " ").find(str) > -1)]["bootcamp_id"].values[0]
            df["bootcamp_id"] = id
            self.load_df_to_table(df , CONFIG.grades.table_id)
        return df

    def load_df_to_table(self,df , table_id):
        dbc = DBConnector()
        df.to_sql(table_id, con=dbc.engine , if_exists="append", index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--load-register', dest='load_register', action='store_true' ,default=False)
    parser.add_argument('--load-grades', dest='load_grades', action='store_true' ,default=False)

    args = parser.parse_args()

    dbl = DBLoader()

    if args.load_register:
        dbl.load_registration_sheet_to_table()
    if args.load_grades:
        dbl.load_grades_to_table()
