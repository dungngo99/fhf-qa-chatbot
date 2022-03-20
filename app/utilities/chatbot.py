from nltk.corpus import stopwords
import nltk
import spacy

nlp = spacy.load("en_core_web_sm")
nltk.download('stopwords')
nltk.download('punkt')
sw = stopwords.words("english")


def read_file(question):
    with open(question, 'r') as file:
        questions = file.readlines()
        return questions


def find_similarity(questions, user):
    user_doc = nlp(user)

    ranks = []
    for idx, question in enumerate(questions):
        question_doc = nlp(question)
        similarity = user_doc.similarity(question_doc)
        ranks.append((idx, similarity))

    sorted_ranks = sorted(ranks, key=lambda x: x[1], reverse=True)
    return sorted_ranks


def answer(ranks):
    f_idx = ranks[0][0]
    return f_idx


if __name__ == "__main__":
    questions = read_file("data/questions.txt")
    ranks = find_similarity(questions, "Can you tell me what an IEP is")
    rank = answer(ranks)
