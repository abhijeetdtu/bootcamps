import unittest
import pandas as pd

from bootcamps.config import CONFIG
from bootcamps.bl.sheet_db_loader import DBLoader

class DBLoaderTests(unittest.TestCase):

    # def test_load_registration_sheet_to_table(self):
    #     dbl = DBLoader()
    #     dbl.load_registration_sheet_to_table()


    def test_load_grades_to_table(self):
        dbl = DBLoader()
        df = dbl.load_grades_to_table()
        print(df.head())

if __name__ == "__main__":
    unittest.main()
