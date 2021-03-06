// Collapsible
var coll = document.getElementsByClassName("collapsible");

for (let i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function () {
    this.classList.toggle("active");

    var content = this.nextElementSibling;

    if (content.style.maxHeight) {
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    }

  });
}

function getTime() {
  let today = new Date();
  hours = today.getHours();
  minutes = today.getMinutes();

  if (hours < 10) {
    hours = "0" + hours;
  }

  if (minutes < 10) {
    minutes = "0" + minutes;
  }

  let time = hours + ":" + minutes;
  return time;
}

// Gets the first message
function firstBotMessage() {
  let firstMessage = "Hi! How can we help you?"
  document.getElementById("botStarterMessage").innerHTML = '<p class="botText"><span>' + firstMessage + '</span></p>';

  let time = getTime();

  $("#chat-timestamp").append(time);
  document.getElementById("userInput").scrollIntoView(false);
}

async function getHardResponse(userText) {
  let botResponse = await getBotResponse(userText);

  if (botResponse['question'] != "") {
    $("#chatbox").append('<p class="botText"><span> Here\'s a commonly asked question we found: </span></p>');
    let questionHtml = '<p class="botText"><span> QUESTION: ' + botResponse['question'] + '</span></p>';
    $("#chatbox").append(questionHtml);
  }

  let botHtml = '<p class="botText"><span>' + botResponse['answer'] + '</span></p>';
  $("#chatbox").append(botHtml);

  if (botResponse['source'] != "") {
    let sourceHtml = '<p class="botText"><span> SOURCE: ' + botResponse['source'] + '</span></p>';
    $("#chatbox").append(sourceHtml);
  }

  document.getElementById("chat-bar-bottom").scrollIntoView(true);
}

function getResponse() {
  let userText = $("#textInput").val();

  if (userText == "") {
    userText = "Hi, I have a question!";
  }

  let userHtml = '<p class="userText"><span>' + userText + '</span</p>';

  $("#textInput").val("");
  $("#chatbox").append(userHtml);
  document.getElementById("chat-bar-bottom").scrollIntoView(true);

  setTimeout(() => {
    getHardResponse(userText);
  }, 1000)
}

function buttonSendText(sampleText) {
  let userHtml = '<p class="userText"><span>' + sampleText + '</span</p>';

  $("#textInput").val("");
  $("#chatbox").append(userHtml);
  document.getElementById("chat-bar-bottom").scrollIntoView(true);
}

function sendButton() {
  getResponse();
}

//Press enter to send message
$("#textInput").keypress(function (e) {
  if (e.which == 13) {
    getResponse();
  }
})
