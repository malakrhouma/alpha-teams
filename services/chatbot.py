import requests
import os
from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("MODEL_NAME", "tinyllama")
OLLAMA_URL = os.getenv("OLLAMA_URL")

history = []

def chat_with_bot(message):

    history.append({
        "role": "user",
        "content": message
    })

    response = requests.post(
        f"{OLLAMA_URL}/api/chat",
        json={
            "model": MODEL,
            "messages": history,
            "stream": False
        }
    )

    data = response.json()

    bot_reply = data["message"]["content"]

    history.append({
        "role": "assistant",
        "content": bot_reply
    })

    return bot_reply