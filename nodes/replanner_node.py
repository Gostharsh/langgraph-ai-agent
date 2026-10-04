# nodes/replanner_node.py

from agents.replanner import replan
from state.agent_state import AgentState


def replanner_node(state):
    print("\nENTERED REPLANNER")

    if not state.reflection.has_failures:
        print("NO FAILURES -> RETURN")
        return state

    new_plan = replan(
        state.question,
        state.reflection.failed_tasks
    )

    state.new_plan = new_plan
    state.plan = new_plan

    print("\nREPLANNER BEFORE")
    print(state.retry_count)

    state.retry_count += 1

    print("\nREPLANNER")

    print("Retry:", state.retry_count)

    return state