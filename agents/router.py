import re
from state.models import Route


def route_question(question):

    q = question.lower().strip()

    match = re.search(
        r"(\d+\s*[\+\-\*/]\s*\d+)",
        q
    )

    if match:

        return Route(
            type="direct",
            tool="calculator",
            input=match.group(1)
        )

    if (
        "what time" in q
        or "current time" in q
        or q == "time"
    ):

        return Route(
            type="direct",
            tool="get_time",
            input=""
        )

    return Route(
        type="planner"
    )