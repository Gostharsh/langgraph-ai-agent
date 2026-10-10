# from rag.build_rag import build_rag

# rag = build_rag()

# def pdf_search(question):
#     return rag.ask(question)

# from rag.services.rag_service import get_rag


# def pdf_search(query):

#     rag = get_rag()

#     return rag.ask(query)


from rag.services.rag_service import get_rag

def pdf_search(query):

    print("\nPDF SEARCH RECEIVED:")
    print(query)

    rag = get_rag()

    result = rag.ask(query)

    print("\nPDF SEARCH RESULT:")
    print(result)

    return result