from bootcamps.bl.dbsetup import DBConnector
from bootcamps.certgen.generate_certs import GenerateCerts
from bootcamps.config import CONFIG

import datetime

class CertSent:

    def generate_certs(self):
        dbconn = DBConnector()
        df = dbconn.execute_sql_file_get_data_frame(CONFIG.cert_send.sql_file)
        hashes = GenerateCerts().generate_certs(df)

        sql_insert = """
        INSERT INTO certificates VALUES('{LOGIN_ID}' , '{BOOTCAMP_ID}' , '{DATETIME}' , '{HASH}')
        """
        
        df.apply(lambda row : dbconn.execute_sql_str(sql_insert.format(**{
        "LOGIN_ID" : row["login_id"] ,
         "BOOTCAMP_ID" : row["bootcamp_id"],
         "DATETIME": datetime.datetime.now(),
         "HASH": hashes[row.name],
        })), axis=1)


if __name__ == "__main__":
    CertSent().generate_certs()
