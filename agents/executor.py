
from tools.registry import TOOLS
from state.models import Observation

def execute_plan(plan):

    observations = []

    for step in plan:

        tool_name = step.tool
        tool_input = step.input

        print(f"\nTool: {tool_name}")
        print(f"Input: {tool_input}")

                # --------------------
        # VALIDATION
        # --------------------

        if tool_name == "pdf_search" and not tool_input.strip():

            observations.append(
                Observation(
                    tool=tool_name,
                    input=tool_input,
                    success=False,
                    result="Empty search query"
                )
            )

            continue

        success = True

        try:

            if tool_name not in TOOLS:
                raise Exception("Unknown tool")

            tool_fn = TOOLS[tool_name]["function"]

            if tool_input:
                result = tool_fn(tool_input)
            else:
                result = tool_fn()

        except Exception as e:

            success = False
            result = str(e)

        observations.append(
            Observation(
                tool=tool_name,
                input=tool_input,
                success=success,
                result=str(result)
            )
        )

    return observations

# =====================================
# REFLECTION
# =====================================

def reflect(observations):

    failed = []

    for obs in observations:

        if not obs.success:
            failed.append(obs)

    return failed