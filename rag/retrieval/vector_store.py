from chromadb.api.models.Collection import Collection
import chromadb
from rag.config import CHROMA_PATH, COLLECTION_NAME, TOP_K , logger
from typing import Any


class VectorStore:

    def __init__(self) -> None:

        client = chromadb.PersistentClient(
            path=CHROMA_PATH
        )

        self.collection: Collection = (
            client.get_or_create_collection(
                name=COLLECTION_NAME
            )
        )

    def load(
        self,
        documents: list[str],
        metadatas: list[dict],
        ids: list[str]
    ) -> None:

        if self.collection.count() > 0:

            logger.info(
                "Collection already contains %s chunks",
                self.collection.count()
            )

            return

        self.collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )

        logger.info(
            "Added %s chunks",
            len(documents)
        )

    def search(
        self,
        query: str,
        top_k: int = TOP_K
    ) -> dict[str, Any]:

        return self.collection.query(
            query_texts=[query],
            n_results=top_k
        )
