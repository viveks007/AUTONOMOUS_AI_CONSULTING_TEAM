from langgraph.graph import StateGraph, END

from graph.state import ConsultingState

from agents.supervisor import supervisor
from agents.business_analyst import business_analyst
from agents.market_researcher import market_researcher
from agents.data_scientist import data_scientist
from agents.solution_architect import solution_architect
from agents.financial_analyst import financial_analyst
from agents.reviewer import reviewer

from graph.parallel_router import parallel_router

#from checkpoint.checkpointer import checkpointer

from checkpoint.sqlite_checkpoint import checkpointer


builder = StateGraph(ConsultingState)

# ----------------------------
# Nodes
# ----------------------------

builder.add_node("supervisor", supervisor)

builder.add_node("business_analyst", business_analyst)
builder.add_node("market_researcher", market_researcher)
builder.add_node("data_scientist", data_scientist)

builder.add_node("solution_architect", solution_architect)
builder.add_node("financial_analyst", financial_analyst)
builder.add_node("reviewer", reviewer)

# ----------------------------
# Entry Point
# ----------------------------

builder.set_entry_point("supervisor")

# ----------------------------
# Parallel Fan-Out
# ----------------------------

builder.add_conditional_edges(
    "supervisor",
    parallel_router
)

# ----------------------------
# Fan-In
# LangGraph waits until all
# incoming branches finish
# ----------------------------

builder.add_edge(
    "business_analyst",
    "solution_architect"
)

builder.add_edge(
    "market_researcher",
    "solution_architect"
)

builder.add_edge(
    "data_scientist",
    "solution_architect"
)

# ----------------------------
# Sequential Flow
# ----------------------------

builder.add_edge(
    "solution_architect",
    "financial_analyst"
)

builder.add_edge(
    "financial_analyst",
    "reviewer"
)

builder.add_edge(
    "reviewer",
    END
)

graph = builder.compile(
    checkpointer=checkpointer
)