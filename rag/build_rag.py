# rag/build_rag.py

from rag.config import PDF_FOLDER
from rag.ingestion.pdf_processor import PDFProcessor
from rag.retrieval.vector_store import VectorStore
from rag.engine import RAGEngine
def build_rag():

    processor = PDFProcessor()

    documents, metadatas, ids = (
        processor.extract(PDF_FOLDER)
    )

    store = VectorStore()

    store.load(
        documents,
        metadatas,
        ids
    )

    return RAGEngine(store)