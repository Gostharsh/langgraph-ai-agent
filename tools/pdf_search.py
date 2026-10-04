from rag import build_rag

rag = build_rag()

def pdf_search(question):
    return rag.ask(question)