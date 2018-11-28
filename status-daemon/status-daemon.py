import time

from core.sheetUploader import GoogleUploader

OAUTH_JSON = 'tempAndHumidity-b4174e738444.json'
GOOGLE_SHEET = "tempsAndHumidity"
INTERVAL = 3

up = GoogleUploader(OAUTH_JSON, GOOGLE_SHEET)

t = time.time()

data = list()
data.append(t)
data.append(23.6)
data.append(56.435)

up.appendToSheet(data, INTERVAL)


'''
def connectToSheet(oauth):
    try:
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth, scope)
        gc = gspread.authorize(credentials)
        sheet = gc.open("tempsAndHumidity").sheet1
        return sheet
    except Exception as e:
        print('Failed to connect to sheet: {}'.format(e))
        raise

sheet = None
while True:
    if sheet == None:
        sheet = connectToSheet(OAUTH_JSON)
    try:
        unique = list()
        unique.append(str(uuid.uuid4()))
        moment = list()
        moment.append(time.time())
        sheet.append_row(moment)
    except Exception as e:
        print('Failed to append_row: {}'.format(e))
        sheet = None  # Reset connection

    time.sleep(PAUSE)
'''
