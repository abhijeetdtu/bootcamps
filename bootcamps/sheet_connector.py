
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pathlib
import pandas as pd

class SheetConnector:

    def __init__(self,path_to_creds=None):
    # If modifying these scopes, delete the file token.pickle.
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
        if path_to_creds is None:
            path_to_creds = os.path.join(pathlib.Path(__file__).absolute().parent , "credentials.json")

        self.path_to_creds = path_to_creds

    def get_creds(self):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.path_to_creds, self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        return creds

    def load_sheet(self,SPREADSHEET_ID , RANGE_NAME):

        creds = self.get_creds()
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                    range=RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
        else:
            print('Name, Major:')
            df = pd.DataFrame(values)
            df.columns = df.iloc[0]
            df.drop(df.index[0], inplace=True)
            print(df.head())

        return df

if __name__ == '__main__':
    Connector().load
