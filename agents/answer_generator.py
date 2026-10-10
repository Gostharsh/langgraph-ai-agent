
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