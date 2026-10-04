# agents/router_node.py

from websockets import route

from agents.router import route_question
from state.agent_state import AgentState


def router_node(
    state: AgentState
) -> AgentState:

    state.route = route_question(
        state.rewritten_question
    )

    return state