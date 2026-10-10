from rag.config import OLLAMA_URL, MODEL_NAME, logger
import requests
import logging


class OllamaClient:

    @staticmethod
    def generate(
        prompt: str
    ) -> str:

        try:

            response = requests.post(
                OLLAMA_URL,
                json={
                    "model": MODEL_NAME,
                    "prompt": prompt,
                    "stream": False,
                    "temperature": 0
                },
                timeout=120
            )

            response.raise_for_status()

            return response.json()["response"]

        except requests.RequestException as error:

            logger.error(
                "Ollama request failed: %s",
                error
            )

            return str(error)