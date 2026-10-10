from rag.llm.ollama_client import OllamaClient
from rag.prompts.answer_prompt import (
    build_answer_prompt
)


class AnswerGenerator:

    def generate(
        self,
        question,
        docs,
        metas
    ):

        context = "\n\n".join(
            (
                f"Source: {meta['source']}\n"
                f"Page: {meta['page']}\n\n"
                f"{doc}"
            )
            for doc, meta in zip(
                docs,
                metas
            )
        )

        prompt = build_answer_prompt(
            question,
            context
        )

        return OllamaClient.generate(prompt)