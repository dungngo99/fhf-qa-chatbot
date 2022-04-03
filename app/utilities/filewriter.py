import gspread
import logging
from oauth2client.service_account import ServiceAccountCredentials

logger = logging.Logger(__name__)

def newRead():
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    # access the json key you downloaded earlier
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "../app/testkey.json", scopes)

    # authenticate the JSON key with gspread
    file = gspread.authorize(credentials)

    # open sheet
    sheet = file.open("QA Window")

    # replace sheet_name with the name that corresponds to yours, e.g, it can be sheet1
    questions_col = sheet.sheet1.col_values(1)

    with open('../app/data/questions.txt', 'w') as f:
        f.write("\n".join(questions_col[1:]))

    logger.info("Successfully updated questions.txt")

    acronyms = {}

    acronym_col = sheet.worksheet("Sheet2").col_values(1)
    translated_col = sheet.worksheet("Sheet2").col_values(2)
    for i in range(1, len(acronym_col)-1):
        acronyms[acronym_col[i]] = translated_col[i]

    logger.info("Created acronym dictionary")

    return acronyms


def findAnswer(a_index):
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    # access the json key you downloaded earlier
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "./app/testkey.json", scopes
    )

    # authenticate the JSON key with gspread
    file = gspread.authorize(credentials)

    # open sheet
    sheet = file.open("QA Window")

    # replace sheet_name with the name that corresponds to yours, e.g, it can be sheet1
    answers_col = sheet.sheet1.col_values(2)
    sources_col = sheet.sheet1.col_values(3)

    return [answers_col[a_index + 1] if a_index+1 < len(answers_col) else "Can't find the answer. Please try again!",
            sources_col[a_index+1] if a_index+1 < len(sources_col) else ""]
