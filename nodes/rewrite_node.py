from agents.query_rewriter import rewrite_query
# from memory.memory import memory``
from state.agent_state import AgentState



# def rewrite_node(
#     state: AgentState
# ) -> AgentState:



#     state.history = memory.get_history()
#     print("\nMEMORY RECEIVED")
#     print(state.history)

#     state.rewritten_question = rewrite_query(
#         state.question,
#         state.history
#     )

#     return state

def rewrite_node(state):

    print("\nMEMORY RECEIVED")
    print(state.history)

    state.rewritten_question = rewrite_query(
        state.question,
        state.history
    )
    print("\nREWRITTEN QUESTION")
    print(state.rewritten_question)

    return state