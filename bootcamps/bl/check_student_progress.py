import pandas as pd
from bootcamps.bl.dbsetup import DBConnector

dbcon = DBConnector()
df = (pd.read_sql(""" select * from grades_tracker""" , dbcon.engine))

df.head()

df.to_csv("./grades_tracker_export.csv")
from bootcamps.bl.dbsetup import DBConnector

class CheckStudentProgress:

    def update_registration_status(self):
        dbc = DBConnector()
                bootcamps = pd.read_sql_table(CONFIG.bootcamps.table_id, con=dbc.engine)
