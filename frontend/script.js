const questionInput = document.getElementById("questionInput");
const askButton = document.getElementById("askButton");
const chatBox = document.getElementById("chatBox");


function addMessage(message, type, sources = []) {

    const messageDiv = document.createElement("div");
    messageDiv.className = `message ${type}`;

    const contentDiv = document.createElement("div");
    contentDiv.className = "message-content";

    const textDiv = document.createElement("div");
    textDiv.textContent = message;

    contentDiv.appendChild(textDiv);


    if (sources.length > 0) {

        const sourcesDiv = document.createElement("div");
        sourcesDiv.className = "sources";

        const title = document.createElement("strong");
        title.textContent = "Sources";

        sourcesDiv.appendChild(title);


        sources.forEach(source => {

            const sourceItem = document.createElement("div");

            sourceItem.textContent =
                `📄 ${source.source} — Page ${source.page}`;

            sourcesDiv.appendChild(sourceItem);
        });


        contentDiv.appendChild(sourcesDiv);
    }


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

        const response = await fetch(
            "http://127.0.0.1:8000/ask",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    question: question
                })
            }
        );


        if (!response.ok) {
            throw new Error("Request failed");
        }


        const data = await response.json();

        addMessage(
            data.answer,
            "bot",
            data.sources
        );


    } catch (error) {

        console.error(error);

        addMessage(
            "Sorry, something went wrong while contacting the server.",
            "bot"
        );

    } finally {

        askButton.disabled = false;
        askButton.textContent = "Ask";
    }
}


askButton.addEventListener(
    "click",
    askQuestion
);


questionInput.addEventListener(
    "keydown",
    function(event) {

        if (event.key === "Enter" && !event.shiftKey) {

            event.preventDefault();

            askQuestion();
        }
    }
);