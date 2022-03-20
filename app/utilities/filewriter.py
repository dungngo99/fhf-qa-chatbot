import gspread
from oauth2client.service_account import ServiceAccountCredentials


def newRead():
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    # access the json key you downloaded earlier
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "testkey.json", scopes)

    # authenticate the JSON key with gspread
    file = gspread.authorize(credentials)

    # open sheet
    sheet = file.open("QA Window")

    # replace sheet_name with the name that corresponds to yours, e.g, it can be sheet1
    questions_col = sheet.sheet1.col_values(1)

    with open('data/questions.txt', 'w') as f:
        f.write("\n".join(questions_col[1:]))

    print("Successfully updated questions.txt")


def findAnswer(a_index):
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    # access the json key you downloaded earlier
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "testkey.json", scopes
    )

    # authenticate the JSON key with gspread
    file = gspread.authorize(credentials)

    # open sheet
    sheet = file.open("QA Window")

    # replace sheet_name with the name that corresponds to yours, e.g, it can be sheet1
    answers_col = sheet.sheet1.col_values(2)
    sources_col = sheet.sheet1.col_values(3)

    print(answers_col[a_index + 1])

    return [answers_col[a_index + 1], sources_col[a_index+1]]
