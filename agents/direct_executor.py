from tools.registry import TOOLS
from state.models import Observation


def execute_direct(route):

    tool_name = route.tool
    tool_input = route.input

    tool_fn = TOOLS[tool_name]["function"]

    try:

        if tool_input:
            result = tool_fn(tool_input)
        else:
            result = tool_fn()

        return [
            Observation(
                tool=tool_name,
                input=tool_input,
                success=True,
                result=str(result)
            )
        ]

    except Exception as e:

        return [
            Observation(
                tool=tool_name,
                input=tool_input,
                success=False,
                result=str(e)
            )
        ]