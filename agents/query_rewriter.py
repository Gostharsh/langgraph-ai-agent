from llm.generate import generate


def rewrite_query(question, history):

    if not history:
        return question

    prompt = f"""
You are a query rewriting agent.

Conversation History:
{history}

Current User Question:
{question}

Task:

If the current question depends on previous context,
rewrite it into a fully self-contained question.

Examples:

Previous:
What is savings?

Current:
Explain more

Rewrite:
Explain more about savings

Previous:
What is investing?

Current:
Give examples

Rewrite:
Give examples of investing

If the question is already complete,
return it unchanged.

Return ONLY the rewritten question.
"""

    rewritten = generate(prompt)

    return rewritten.strip()