from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# historique des messages
messages = [
    {
        "role": "system",
        "content": "You are a helpful chatbot for teaching computer science basics."
    }
]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    # nzid message utilisateur
    messages.append({
        "role": "user",
        "content": user_message
    })

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "tinyllama",
            "messages": messages,
            "stream": False
        }
    )

    data = response.json()

    bot_reply = data["message"]["content"]

    # nzid réponse assistant lel historique
    messages.append({
        "role": "assistant",
        "content": bot_reply
    })

    return jsonify({
        "reply": bot_reply
    })


if __name__ == "__main__":
    app.run(debug=True)