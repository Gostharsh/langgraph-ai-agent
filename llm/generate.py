import requests
from config import OLLAMA_URL, MODEL_NAME

def generate(prompt):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "temperature": 0
        }
    )

    response.raise_for_status()

    return response.json()["response"]