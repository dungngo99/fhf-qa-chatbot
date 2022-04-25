from typing import Dict
import spacy
import pandas as pd
import asyncio

from app.utilities import filewriter

nlp = spacy.load("en_core_web_md")
THRESHOLD = 0.8


async def find_answer(user: str) -> Dict:
    """A core function to find the most similar answer to the user's question

    Args:
        user (str): a user's question

    Returns:
        Dict: a pair result of an answer and a source
    """
    # Read a csv file and convert it to a dataframe
    df = pd.read_csv("app/data/data.csv").fillna(value="")
    df_acronyms = pd.read_csv('app/data/acronyms.csv')

    acronyms = {}
    for i in range(len(df_acronyms)):
        acronyms[df_acronyms.iloc[i, 0]] = df_acronyms.iloc[i, 1]

    # create a Doc object
    user_doc = nlp(filewriter.expand_acronyms(acronyms, user))

    # A list of similarity scores
    ranks = []

    # Iterate through each question and compute its similarity score with a given user's question
    for idx, question in enumerate(df['questions'].values):
        if question == "":
            ranks.append((idx, 0))
            continue

        question_doc = nlp(question)
        similarity = user_doc.similarity(question_doc)
        ranks.append((idx, similarity))

    # Sort the similarity scores to find the most similar question
    sorted_ranks = sorted(ranks, key=lambda x: x[1], reverse=True)

    # if the most similar score does not pass the threshold, return None
    if sorted_ranks[0][1] < THRESHOLD:
        return {"question": "", "answer": "We weren't able to match your question. Try rephrasing!", "source": ""}

    best_idx = sorted_ranks[0][0]
    return {"question": df.iloc[best_idx, 3], "answer": df.iloc[best_idx, 1], "source": df.iloc[best_idx, 2]}


if __name__ == "__main__":
    answer = asyncio.run(find_answer("Can you tell me what an IEP is"))
    print(answer)
