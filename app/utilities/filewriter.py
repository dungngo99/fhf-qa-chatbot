from typing import List
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


def expand_acronyms(acronyms, question):
    question = question.replace("?", "")
    question = question.replace("!", "")
    question = question.replace(".", "")
    word_list = question.split()

    for i in range(len(word_list)):
        if word_list[i].strip() in acronyms:
            word_list[i] = acronyms[word_list[i]]

    question = " ".join(word_list)

    return question


def save_acronyms(sheet):
    data = {'acronyms': [], 'translated_col': []}

    acronym_col = sheet.worksheet("Sheet2").col_values(1)
    translated_col = sheet.worksheet("Sheet2").col_values(2)

    for i in range(1, len(acronym_col)-1):
        data['acronyms'].append(acronym_col[i])
        data['translated_col'].append(translated_col[i])

    pd.DataFrame(data).to_csv('app/data/acronyms.csv', index=False)


def save_data(sheet):
    questions_col = sheet.sheet1.col_values(1)
    answers_col = sheet.sheet1.col_values(2)
    sources_col = sheet.sheet1.col_values(3)

    # Make all lists to have the same length
    max_length = max([len(questions_col), len(answers_col), len(sources_col)])
    questions_col += [""]*(max_length-len(questions_col))
    answers_col += [""]*(max_length-len(answers_col))
    sources_col += [""]*(max_length-len(sources_col))

    df = pd.read_csv('app/data/acronyms.csv')
    acronyms = {}
    for i in range(len(df)):
        acronyms[df.iloc[i,0]] = df.iloc[i,1]

    for i in range(1, len(questions_col)-1):
        questions_col[i] = expand_acronyms(acronyms, questions_col[i])

    data = {
        "questions": questions_col[1:],
        "answers": answers_col[1:],
        "sources": sources_col[1:]
    }

    pd.DataFrame(data).fillna(value="").to_csv("app/data/data.csv", index=False)


async def fetchGoogleSheet():
    """A function to fetch data from Google sheet to update local data source
    """
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    # access the json key downloaded earlier
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "app/testkey.json", scopes)

    # authenticate the JSON key with gspread
    file = gspread.authorize(credentials)

    # open sheet
    sheet = file.open("QA Window")

    save_acronyms(sheet)
    save_data(sheet)


def findAnswer(a_index: int) -> List[str]:
    """A function to find a corresponding answer to a given index

    Args:
        a_index (int): a question's index

    Returns:
        List[str]: a pair of an answer and a source that corresponds to a given index
    """
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    # access the json key downloaded earlier
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "./app/testkey.json", scopes
    )

    # authenticate the JSON key with gspread
    file = gspread.authorize(credentials)

    # open sheet
    sheet = file.open("QA Window")

    # replace sheet_name with the name that corresponds to yours, e.g, it can be sheet1
    questions_col = sheet.sheet1.col_values(1)
    answers_col = sheet.sheet1.col_values(2)
    sources_col = sheet.sheet1.col_values(3)

    return [answers_col[a_index + 1] if a_index+1 < len(answers_col) else "Can't find the answer. Please try again!",
            sources_col[a_index+1] if a_index+1 < len(sources_col) else "",
            questions_col[a_index+1] if a_index+1 < len(questions_col) else ""]
