from rag.retrieval.vector_store import VectorStore
from rag.retrieval.retriever import Retriever
from rag.generation.answer_generator import (
    AnswerGenerator
)

class RAGEngine:

    def __init__(
        self,
        store: VectorStore
    ) -> None:
        self.retriever = Retriever(store)
        self.generator = AnswerGenerator()

    def ask(
        self,
        question: str
    ) -> str:

        filtered_docs, filtered_metas = (
            self.retriever.retrieve(question)
        )

        answer = self.generator.generate(
            question,
            filtered_docs,
            filtered_metas
        )

        return answer