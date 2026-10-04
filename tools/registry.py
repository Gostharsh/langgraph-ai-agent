from tools.calculator import calculator
from tools.time_tool import get_time
from tools.pdf_search import pdf_search

TOOLS = {
    "calculator": {
        "function": calculator,
        "description": "Perform mathematical calculations"
    },
    "get_time": {
        "function": get_time,
        "description": "Get current local time"
    },
    "pdf_search": {
        "function": pdf_search,
        "description": "Search document knowledge base"
    }
}


from tools.registry import TOOLS

def build_tool_prompt(route=None):

    if route:

        tool = TOOLS.get(route)

        if tool:

            return (
                f"{route} - "
                f"{tool['description']}"
            )

    lines = []

    for name, info in TOOLS.items():

        lines.append(
            f"{name} - {info['description']}"
        )

    return "\n".join(lines)