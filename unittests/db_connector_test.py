import unittest

from bootcamps.bl.dbsetup import DBConnector
from bootcamps.config import CONFIG

class DBConnectorTests(unittest.TestCase):

    def test_execute_sql_file(self):
        dbconn = DBConnector()
        df = dbconn.execute_sql_file_get_data_frame(CONFIG.cert_send.sql_file)
        self.assertEqual(df.shape[1] , 10)

if __name__ == '__main__':
    unittest.main()
