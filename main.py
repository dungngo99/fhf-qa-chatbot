from flask import Flask
from flask import request
from flask_cors import CORS

from utilities.chatbot import read_file, find_similarity, answer
from utilities.filewriter import findAnswer, newRead

app = Flask(__name__)
CORS(app)


@app.route("/answer", methods=['POST'])
def answer_endpoint():
    newRead()

    questions = read_file("data/questions.txt")
    message = request.json['message']

    ranks = find_similarity(questions, message)
    a_index = answer(ranks)

    return findAnswer(a_index)


if __name__ == '__main__':
    app.run(debug=True)
