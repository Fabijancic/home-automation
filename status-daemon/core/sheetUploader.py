import json
import sys
import time
import datetime
import uuid

import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GoogleUploader:
    ''' Contains functionality for connecting to google and uploading data
    '''
    def __init__(self, auth, google_sheet):
        self.OAUTH = auth
        self.google_sheet = google_sheet
        self.sheet = None

    def _connectToSheet(self):
        ''' Connect and return a sheet object
        '''
        try:
            scope = ['https://spreadsheets.google.com/feeds',
                    'https://www.googleapis.com/auth/drive']
            credentials = ServiceAccountCredentials.from_json_keyfile_name(
                self.OAUTH, scope)
            gc = gspread.authorize(credentials)
            self.sheet = gc.open(self.google_sheet).sheet1
            return self.sheet
        except Exception as e:
            print('Failed to connect to sheet: {}'.format(e))
            return False

    def appendToSheet(self, data):
        ''' Upload data as a row to google spreadsheet
            Input: data = list, INTERVAL - seconds
        '''
        # Check the connection
        if not self._connectToSheet():
            self._connectToSheet()

        try:
            # Check the input data
            if not isinstance(data, list):
                data = [data]
            
            # Do the upload
            row = list()
            for item in data:
                row.append(item)
            self.sheet.append_row(row)
        except Exception as e:
            print('Failed to append_row: {} with error: {}'.format(row[0], e))
            self.sheet = None  # Reset connection




