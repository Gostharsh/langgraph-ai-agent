# from rag.llm.ollama_client import OllamaClient


# class QueryRewriter:

#     def __init__(self):
#         self.last_question = ""

#     def is_followup(
#         self,
#         question: str
#     ) -> bool:

#         followup_words = {
#             "it",
#             "its",
#             "they",
#             "them",
#             "this",
#             "that",
#             "those"
#         }

#         words = question.lower().split()

#         return any(
#             word in followup_words
#             for word in words
#         )

#     def rewrite(
#         self,
#         current_question: str
#     ) -> str:

#         if not self.is_followup(current_question):
#             self.last_question = current_question
#             return current_question

#         if not self.last_question:
#             return current_question

#         prompt = f"""
# Previous Question:
# {self.last_question}

# Current Question:
# {current_question}

# Rewrite the current question
# so it is fully self-contained.

# Keep the meaning exactly the same.

# Return ONLY the rewritten question.
# """

#         rewritten = OllamaClient.generate(prompt)

#         self.last_question = current_question

#         return rewritten.strip()