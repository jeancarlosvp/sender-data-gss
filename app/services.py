import gspread

def get_worksheet(credentials, book_id, sheet_name):
    gc = gspread.service_account_from_dict(credentials)
    book = gc.open_by_key(book_id)
    worksheet = book.worksheet(sheet_name)
    return worksheet
