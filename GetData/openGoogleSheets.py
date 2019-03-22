# -*- coding: utf-8 -*-
"""
Open Google Sheet

"""

from googleapiclient.discovery import build

import json

with open("../gsSecret.json", "r") as secretJSON:
    secretDict = json.load(secretJSON)
    GOOGLE_SHEETS_API_KEY = secretDict["API_KEY"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1SMfMj8Q8jL1s5OUGOu91DeqCcLPVgw3Ze8Vp_mLzbxc'
SAMPLE_RANGE_NAME = 'Brexit!A1:B5'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
            

    service = build('sheets', 'v4', developerKey = GOOGLE_SHEETS_API_KEY)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Number:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[1]))

if __name__ == '__main__':
    main()