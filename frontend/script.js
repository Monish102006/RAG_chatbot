const questionInput = document.getElementById("questionInput");
const askButton = document.getElementById("askButton");
const chatBox = document.getElementById("chatBox");


function addMessage(message, type) {

    const messageDiv = document.createElement("div");
    messageDiv.className = `message ${type}`;

    const contentDiv = document.createElement("div");
    contentDiv.className = "message-content";

    contentDiv.textContent = message;

    messageDiv.appendChild(contentDiv);
    chatBox.appendChild(messageDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}


async function askQuestion() {

    const question = questionInput.value.trim();

    if (!question) {
        return;
    }

    addMessage(question, "user");

    questionInput.value = "";
    askButton.disabled = true;
    askButton.textContent = "Asking...";

    try {

        const response = await fetch("http://127.0.0.1:8000/ask", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })
        });


        if (!response.ok) {
            throw new Error("Request failed");
        }


        const data = await response.json();

        addMessage(data.answer, "bot");

    } catch (error) {

        addMessage(
            "Sorry, something went wrong while contacting the server.",
            "bot"
        );

        console.error(error);

    } finally {

        askButton.disabled = false;
        askButton.textContent = "Ask";
    }
}


askButton.addEventListener("click", askQuestion);


questionInput.addEventListener("keydown", function(event) {

    if (event.key === "Enter" && !event.shiftKey) {

        event.preventDefault();

        askQuestion();
    }

});