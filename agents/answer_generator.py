
# from llm.generate import generate
# from utils.observation_utils import (
#     get_successful_observations
# )
# def generate_final_answer(
#     question,
#     observations
# ):

#     successful =  get_successful_observations(
#         observations
#     )

#     if not successful:
#         return "I could not find an answer."


    

#     prompt = f"""
# You are an Answer Generation Agent.

# USER QUESTION:
# {question}

# TOOL RESULTS:
# {successful}

# RULES:

# 1. Use ONLY information from TOOL RESULTS.

# 2. Do NOT use outside knowledge.

# 3. Do NOT invent facts.

# 4. Do NOT add examples unless they appear in TOOL RESULTS.

# 5. Do NOT answer questions that were not asked.

# 6. If TOOL RESULTS are insufficient, say:

# "I could not find enough information."

# 7. Be concise and factual.

# Generate the final answer.
# """

#     return generate(prompt).strip()



from utils.observation_utils import (
    get_successful_observations
)

def generate_final_answer(
    question,
    observations
):

    successful = get_successful_observations(
        observations
    )

    if not successful:
        return "I could not find an answer."

    parts = []

    for obs in successful:

        if obs.tool == "calculator":

            parts.append(
                f"The result is {obs.result}."
            )

        elif obs.tool == "get_time":

            parts.append(
                f"The current time is {obs.result}."
            )

        elif obs.tool == "pdf_search":

            parts.append(
                obs.result
            )

    return "\n".join(parts)