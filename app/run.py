from flask import Flask
from flask import request

from app.utilities import chatbot
from app.utilities import filewriter

fhf_qa_chatbot = Flask(__name__)


@fhf_qa_chatbot.route("/")
def index():
    return "<h1>Welcome to our app, FHF QA Chatbot!</h1>"

@fhf_qa_chatbot.route("/answer", methods=['POST'])
def answer_endpoint():
    filewriter.newRead()

    message = request.json['message']
    questions = chatbot.read_file("data/questions.txt")

    ranks = chatbot.find_similarity(questions, message)
    a_index = chatbot.answer(ranks)
    answerWithSource = filewriter.findAnswer(a_index)

    return {'answer': answerWithSource[0], 'source': answerWithSource[1]}

if __name__ == "__main__":
    fhf_qa_chatbot.run(debug=True)
