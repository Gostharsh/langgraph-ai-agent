def build_rag_prompt(
    context: str,
    question: str
) -> str:

    return f"""
You are a document assistant.

Answer ONLY using the provided context.

Keep the answer concise.

Mention:
- PDF name
- Page number

Context:
{context}

Question:
{question}

Answer:
"""