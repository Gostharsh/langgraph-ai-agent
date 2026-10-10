from llm.generate import generate


class QueryExpander:

    def expand(self, question: str):

        prompt = f"""
Generate 3 alternative search queries.

Question:
{question}

Rules:
- Preserve exactly the same meaning
- Do not introduce new topics
- Do not narrow the scope
- Do not broaden the scope
- Only create paraphrases
- One query per line
- No numbering
- No explanations
"""

        response = generate(prompt)

        queries = [
            q.strip()
            for q in response.split("\n")
            if q.strip()
        ]

        return [question] + queries