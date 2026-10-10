# from langgraph.checkpoint import memory
from langgraph.graph import (
    StateGraph,
    START,
    END
)

from state.agent_state import AgentState

from nodes.rewrite_node import rewrite_node
from nodes.router_node import router_node
from nodes.executor_node import executor_node
from nodes.planner_node import planner_node
from nodes.reflector_node import reflector_node
from nodes.replanner_node import replanner_node
from nodes.answer_node import answer_node
from graph.reflection_edges import reflection_decision
from graph.conditional_edges import route_decision
from langgraph.checkpoint.memory import MemorySaver



builder = StateGraph(AgentState)

builder.add_node("rewrite", rewrite_node)

builder.add_node("router", router_node)

builder.add_node("executor", executor_node)

builder.add_node("planner", planner_node)

builder.add_node("reflector", reflector_node)

builder.add_node("replanner", replanner_node)

builder.add_node("answer", answer_node)

# builder.add_node("memory", memory_node)

builder.add_edge(START, "rewrite")


builder.add_edge("rewrite", "router")

builder.add_edge("planner", "executor")

builder.add_edge("executor", "reflector")

builder.add_conditional_edges(
    "reflector",
    reflection_decision,
    {
        "answer": "answer",
        "replan": "replanner",
    }
)

builder.add_conditional_edges(
    "router",
    route_decision,
    {
        "direct": "executor",
        "planner": "planner",
    }
)




builder.add_edge("replanner","executor")

builder.add_edge("answer", END)

memory = MemorySaver()

graph = builder.compile(
    checkpointer=memory
)

