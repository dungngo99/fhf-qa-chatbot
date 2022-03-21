async function getBotResponse(input) {
  // Simple responses
  if (input == "hello" || input == "Hello" || input == "hi" || input == "Hi" || input == "test") {
    return { "answer": ["Hello there!"], "source": "" };
  } else if (input == "goodbye" || input == "Goodbye" || input == "bye" || input == "Bye") {
    return { "answer": ["Let us know if you need anything else!"], "source": "" };
  } else if (input == "Hi, I have a question!") {
    return { "answer": ["What's the question? Maybe we can help!"], "source": "" };
  } else {
    let url = 'http://0.0.0.0:5000/answer';
    let data = { "message": input };

    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })
      if (response.status === 200) {
        const responseBot = await response.json();
        return responseBot;
      }
    } catch (error) {
      console.log(error);
    }
    return null;
  }
}
