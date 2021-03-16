from sqlalchemy import create_engine
import sqlite3
import pathlib
import os
# Create Registration Table

import pandas as pd

from bootcamps.config import CONFIG


class DBConnector:
    def __init__(self):
        self.engine = create_engine(CONFIG.db_path, echo=False)
        self.conn = sqlite3.connect('bootcamp.db')
        self.cursor = self.conn.cursor()


    def get_path(self , fname):
        return os.path.join(pathlib.Path(__file__).absolute().parent.parent ,"sql", fname)

    def get_sql_string(self,sql_file):
        with open(self.get_path(sql_file)) as sql_file:
            sql_as_string = sql_file.read()
        return sql_as_string

    def execute_sql_str(self, sql_str):
        self.cursor.executescript(sql_str)

    def execute_sql_file(self,sql_file):
        sql_as_string = self.get_sql_string(sql_file)
        self.cursor.executescript(sql_as_string)

    def execute_sql_file_get_data_frame(self,sql_file):
        sql_as_string = self.get_sql_string(sql_file)
        return pd.read_sql(sql_as_string , self.engine)

    def setup(self):
        self.execute_sql_file(CONFIG.bootcamps.sql_file)
        self.execute_sql_file(CONFIG.registration.sql_file)
        self.execute_sql_file(CONFIG.grades.sql_file)
        self.execute_sql_file(CONFIG.grades_tracker.sql_file)
        self.execute_sql_file(CONFIG.registration_process.sql_file)
        self.execute_sql_file(CONFIG.certificates.sql_file)


if __name__ == "__main__":
    setup_wiz = DBConnector()
    setup_wiz.setup()
