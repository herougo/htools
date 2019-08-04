

def google_sheet_to_table():
    # https://developers.google.com/sheets/api/quickstart/python
    # pip install gspread oauth2client

    import gspread
    from oauth2client.service_account import ServiceAccountCredentials


    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("Copy of Legislators 2017").sheet1

    # Extract and print all of the values
    list_of_hashes = sheet.get_all_records()
    print(list_of_hashes)

    sheet.get_all_values()
    Or you could just pull the data from a single row, column, or cell:

    sheet.row_values(1)

    sheet.col_values(1)

    sheet.cell(1, 1).value

    sheet.update_cell(1, 1, "I just wrote to a spreadsheet using Python!")

def 