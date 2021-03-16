import unittest

from bootcamps.sheet_connector import SheetConnector

class ConnectorTests(unittest.TestCase):

    def test_connection(self):
        file_id = "1zdInYO4atUXeTZhGwssc7EizJvZ1WzP0f1FkIs0p3X8"
        sheet = "Form Responses 1"
        conn  =SheetConnector()
        df = conn.load_sheet(file_id, sheet)
        df = df.dropna(axis=1)
        print(df.columns)
        df.to_csv("test.csv")



if __name__ == "__main__" :
    unittest.main()
