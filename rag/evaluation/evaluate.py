from rag.evaluation.questions import QUESTIONS
from rag.services.rag_service import get_rag

rag = get_rag()

for q in QUESTIONS:

    print("\n" + "=" * 50)

    print("QUESTION:", q)

    docs, metas = rag.retriever.retrieve(q)

    print("\nTOP CHUNK:\n")

    print(docs[0][:500])