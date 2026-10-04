# from llm.generate import generate
# from utils.json_utils import extract_json
# from tools.registry import build_tool_prompt
# from prompts.planner_prompt import build_planner_prompt



# def create_plan(question):

#     tool_text = build_tool_prompt()
#     prompt = build_planner_prompt(
#         question,
#         tool_text
#     )

#         # tool_text = build_tool_prompt()


#     response = generate(prompt)

#     print("\nRAW PLAN RESPONSE:")
#     print(response)

#     plan = extract_json(response)

#     return plan

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

    plan = extract_json(response)

    return plan

    