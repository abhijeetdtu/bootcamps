import pandas as pd

from bootcamps.bl.dbsetup import DBConnector

class CheckStudentProgress:

    def update_registration_status(self):
        dbc = DBConnector()
                bootcamps = pd.read_sql_table(CONFIG.bootcamps.table_id, con=dbc.engine)
