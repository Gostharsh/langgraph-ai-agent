from pathlib import Path
import os
import logging
from sentence_transformers import CrossEncoder

PDF_FOLDER = Path(os.getenv("PDF_FOLDER", r"D:\GEN_AI\pdfs"))

CHROMA_PATH = os.getenv("CHROMA_PATH", "./chroma_db")

COLLECTION_NAME = os.getenv("COLLECTION_NAME", "multi_pdf_rag")

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 300))

CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 50))

TOP_K = int(os.getenv("TOP_K", 15))

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "llama3.2"
)

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/generate"
)

RERANKER_MODEL = (
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)

reranker = CrossEncoder(
    RERANKER_MODEL
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)