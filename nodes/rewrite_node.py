from agents.query_rewriter import rewrite_query
from memory.memory import memory
from state.agent_state import AgentState



def rewrite_node(
    state: AgentState
) -> AgentState:

    state.history = memory.get_history()

    state.rewritten_question = rewrite_query(
        state.question,
        state.history
    )

    return state