# state/state_factory.py
from state.agent_state import AgentState


def create_state(question: str) -> AgentState:

    return AgentState(
        question=question
    )