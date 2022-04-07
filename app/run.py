import asyncio
from flask import Flask, request, render_template
from flask_cors import CORS

from app.utilities import chatbot
from app.utilities import filewriter

fhf_qa_chatbot = Flask(__name__)
CORS(fhf_qa_chatbot, resources={r"*": {"origins": "*"}})


@fhf_qa_chatbot.route("/")
def index():
    return render_template('index.html')


@fhf_qa_chatbot.route("/answer", methods=['POST'])
def answer_endpoint():
    message = request.json['message']

    async def run_tasks():
        asyncio.create_task(filewriter.fetchGoogleSheet())
        findAnswerTask = asyncio.create_task(chatbot.find_answer(message))

        answer = await findAnswerTask
        return answer

    return asyncio.run(run_tasks())


if __name__ == "__main__":
    fhf_qa_chatbot.run(debug=True)
