from flask import Flask, request, render_template, send_from_directory

from utilities import chatbot
from utilities import filewriter
from flask_cors import CORS

fhf_qa_chatbot = Flask(__name__)
CORS(fhf_qa_chatbot, resources={r"*": {"origins": "*"}})

@fhf_qa_chatbot.route("/")
def index():
    return render_template('index.html')

@fhf_qa_chatbot.route("/answer", methods=['POST'])
def answer_endpoint():
    acronyms = filewriter.newRead()
    logger.info("Created acronym dictionary")

    message = request.json['message']
    message = filewriter.expand_acronyms(acronyms, message)

    questions = chatbot.read_file("./app/data/questions.txt")

    ranks = chatbot.find_similarity(questions, message)

    if len(ranks) == 0:
        return {'answer': "Can't find an answer. Try rephrasing, or call (504) 888-9111 to get help!", "source": ""}

    a_index = chatbot.answer(ranks)
    answerWithSource = filewriter.findAnswer(a_index)

    return {'answer': answerWithSource[0], 'source': answerWithSource[1]}


if __name__ == "__main__":
    fhf_qa_chatbot.run(debug=True)
