import spacy
nlp = spacy.load("en_core_web_trf")

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from scipy.spatial.distance import cosine
from pathlib import Path
import glob

tfidf_vectorizer = TfidfVectorizer(stop_words="english")



def read_file(question):
    with open(question, 'r') as file:
        questions = file.readlines()
        return questions

tfidf_vector = tfidf_vectorizer.fit_transform(read_file('questions.txt'))

def find_similarity(questions, user):
    user_doc = tfidf_vectorizer.transform([user]).toarray().flatten()

    ranks = []
    for idx, question in enumerate(questions):
        print(question)
        question_doc = tfidf_vectorizer.transform([question]).toarray().flatten()
        similarity = 1.0 - cosine(question_doc, user_doc)
        ranks.append((idx, similarity))

    sorted_ranks = sorted(ranks, key=lambda x: x[1], reverse=True)

    return sorted_ranks


def answer(ranks):
    f_idx = ranks[0][0]
    return f_idx
