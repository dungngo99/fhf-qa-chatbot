from re import I
from flask import Flask
from flask import request
from flask_cors import CORS

from filewriter import newRead, findAnswer
from chatbot import read_file, find_similarity, answer

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Welcome to our app, FHF QA Chatbot!"


@app.route("/answer", methods=['POST'])
def answer_endpoint():
    newRead()

    questions = read_file("data/questions.txt")
    message = request.json['message']

    ranks = find_similarity(questions, message)
    a_index = answer(ranks)

    return findAnswer(a_index)


if __name__ == "__main__":
    app.run(debug=True)
