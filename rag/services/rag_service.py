from rag.build_rag import build_rag

_rag_instance = None


def get_rag():

    global _rag_instance

    if _rag_instance is None:
        print("Loading RAG...")

        _rag_instance = build_rag()

    return _rag_instance