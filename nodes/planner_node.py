from agents.planner import create_plan
from agents.validator import validate_plan
from state.agent_state import AgentState
from state.models import PlanStep

# def planner_node(
#         state: AgentState
#         ) -> AgentState:

#     state.plan = create_plan(
#         state.rewritten_question,
#         state.history
#     )

#     state.plan = validate_plan(
#         state.plan
#     )

#     return state

def planner_node(
    state: AgentState
) -> AgentState:

    raw_plan = create_plan(
        state.rewritten_question,
        state.history
    )

    raw_plan = validate_plan(
        raw_plan
    )

    state.plan = [
        PlanStep(
            tool=step["tool"],
            input=step.get("input", "")
        )
        for step in raw_plan
    ]

    for step in state.plan:
        print(type(step))

    return state