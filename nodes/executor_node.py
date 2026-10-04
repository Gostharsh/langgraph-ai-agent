# nodes/executor_node.py

from agents.executor import execute_plan
from agents.direct_executor import execute_direct
from state.agent_state import AgentState

def executor_node(
    state: AgentState
) -> AgentState:

    route = state.route

    # Direct execution path
    if route.type == "direct":

        observations = execute_direct(route)

        state.observations = observations

        return state

    # Planner path
    plan = state.plan

    observations = execute_plan(plan)

    state.observations = observations

    print("\nEXECUTOR")

    return state