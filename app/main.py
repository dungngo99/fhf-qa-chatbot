from re import I
from flask import Flask
from flask import request
from flask_cors import CORS

from app.utilities import chatbot
from app.utilities import filewriter

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Welcome to our app, FHF QA Chatbot!"


@app.route("/answer", methods=['POST'])
def answer_endpoint():
    filewriter.newRead()

    questions = chatbot.read_file("data/questions.txt")
    message = request.json['message']

    ranks = chatbot.find_similarity(questions, message)
    a_index = chatbot.answer(ranks)

    return filewriter.findAnswer(a_index)


if __name__ == "__main__":
    app.run(debug=True)
