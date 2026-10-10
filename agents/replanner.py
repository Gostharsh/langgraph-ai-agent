from urllib import response

from llm.generate import generate
from tools.registry import build_tool_prompt
from utils.json_utils import extract_json


def replan(question, failed_tasks):

    tool_text = build_tool_prompt()

    prompt = f"""
You are a replanning agent.

User Question:
{question}

Available Tools:
{tool_text}

Failed Tasks:
{failed_tasks}

Your job:

1. Analyze why each task failed.
2. Create replacement tasks ONLY if a different tool or input may solve the failure.
3. Do NOT recreate successful tasks.
4. Do NOT add new tasks.
5. Do NOT invent information.
6. If no recovery is possible, return [].

Output must be JSON only.

Example:

[
  {{
    "tool": "pdf_search",
    "input": "savings"
  }}
]

Return ONLY JSON.
"""

    response = generate(prompt)

    print("\nRAW REPLAN RESPONSE")
    print(response)

    plan = extract_json(response)

    valid_plan = []

    for step in plan:

        if (
            isinstance(step, dict)
            and "tool" in step
            and "input" in step
        ):
            valid_plan.append(step)

    return valid_plan

    print("\nPARSED PLAN")
    print(plan)

    if not isinstance(plan, list):
        return []
        return plan