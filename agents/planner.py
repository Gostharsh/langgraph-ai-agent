

from state.models import PlanOutput
from llm.generate import generate
from utils.json_utils import extract_json
from tools.registry import build_tool_prompt
from prompts.planner_prompt import build_planner_prompt


def create_plan(question, history):


    tool_text = build_tool_prompt()

    prompt = build_planner_prompt(
        question,
        tool_text,
        history
    )

    response = generate(prompt)

    print("\nRAW PLAN RESPONSE:")
    print(response)

    parsed = PlanOutput.model_validate_json(
        response
    )

    return parsed.steps

    

    