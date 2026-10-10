
import logging
  
from pathlib import Path

from pypdf import PdfReader

from rag.config import (
    CHUNK_SIZE,     
    CHUNK_OVERLAP,
    logger
)


class PDFProcessor:

    @staticmethod
    def chunk_text(
        text: str,
        chunk_size: int,
        overlap: int
    ) -> list[str]:

        words = text.split()

        if len(words) <= chunk_size:
            return [text]

        step = chunk_size - overlap

        return [
            " ".join(words[i:i + chunk_size])
            for i in range(0, len(words), step)
        ]

    def extract(
        self,
        pdf_folder: Path
    ) -> tuple[list[str], list[dict], list[str]]:

        documents: list[str] = []
        metadatas: list[dict] = []
        ids: list[str] = []

        chunk_id = 1

        pdf_files = list(pdf_folder.glob("*.pdf"))

        if not pdf_files:
            raise FileNotFoundError(
                f"No PDFs found in {pdf_folder}"
            )

        for pdf_file in pdf_files:

            logger.info(
                "Processing %s",
                pdf_file.name
            )

            try:
                reader = PdfReader(str(pdf_file))

                for page_no, page in enumerate(
                    reader.pages,
                    start=1
                ):

                    text = page.extract_text()

                    if not text:
                        continue

                    chunks = self.chunk_text(
                        text=text,
                        chunk_size=CHUNK_SIZE,
                        overlap=CHUNK_OVERLAP
                    )

                    for chunk in chunks:

                        documents.append(chunk)

                        metadatas.append(
                            {
                                "source": pdf_file.name,
                                "page": page_no
                            }
                        )

                        ids.append(str(chunk_id))

                        chunk_id += 1

            except Exception as error:
                logger.error(
                    "Failed reading %s : %s",
                    pdf_file.name,
                    error
                )

        logger.info(
            "Indexed %s chunks",
            len(documents)
        )

        return documents, metadatas, ids