const chatBox = document.getElementById("chat-box");
const sendBtn = document.getElementById("send-btn");
const userInput = document.getElementById("user-input");

function addMessage(sender, text) {

    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message");

    if (sender === "user") {
        messageDiv.classList.add("user-message");
        messageDiv.innerHTML = `
            <div class="message-content">
                <strong>Vous :</strong><br>
                ${text}
            </div>
        `;
    } else {
        messageDiv.classList.add("bot-message");
        messageDiv.innerHTML = `
            <div class="message-content">
                <strong>Bot :</strong><br>
                ${text}
            </div>
        `;
    }

    chatBox.appendChild(messageDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {

    const message = userInput.value.trim();

    if (message === "") return;

    addMessage("user", message);

    userInput.value = "";

    try {

        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        addMessage("bot", data.reply);

    } catch (error) {

        addMessage("bot", "Erreur de connexion avec le serveur.");

        console.error(error);
    }
}

sendBtn.addEventListener("click", sendMessage);

userInput.addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});