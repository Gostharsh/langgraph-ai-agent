from graph.build_graph import graph
from state.agent_state import AgentState

# Direct route test
state = AgentState(
    question="What is 50*4?"
)

result = graph.invoke(state)

print("\nDIRECT TEST")
print(result)

# Planner route test
state = AgentState(
    question="Explain investing"
)

result = graph.invoke(state)

print("\nPLANNER TEST")
print(result)

# from state.agent_state import AgentState
# from state.agent_state import AgentState
# from state.models import PlanStep


# state = AgentState(
#     question="test"
# )

# state.plan.append(
#     PlanStep(
#         tool="pdf_search",
#         input="investing"
#     )
# )

# print(state.plan[0].tool)