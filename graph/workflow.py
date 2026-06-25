from langgraph.graph import (
    StateGraph,
    END
)

from graph.state import ConsultingState
from graph.router import supervisor_router

from agents.supervisor import supervisor

from agents.business_analyst import business_analyst
from agents.market_researcher import market_researcher
from agents.data_scientist import data_scientist
from agents.solution_architect import solution_architect
from agents.financial_analyst import financial_analyst
from agents.reviewer import reviewer

from graph.reducers import merge_analysis


builder = StateGraph(
    ConsultingState
)

builder.add_node(
    "supervisor",
    supervisor
)

builder.add_node(
    "business_analyst",
    business_analyst
)

builder.add_node(
    "market_researcher",
    market_researcher
)

builder.add_node(
    "data_scientist",
    data_scientist
)

builder.add_node(
    "merge_analysis",
    merge_analysis
)

builder.add_node(
    "solution_architect",
    solution_architect
)

builder.add_node(
    "financial_analyst",
    financial_analyst
)

builder.add_node(
    "reviewer",
    reviewer
)

builder.set_entry_point(
    "supervisor"
)

builder.add_conditional_edges(
    "supervisor",
    supervisor_router,
    {
        "business_analyst":
        "business_analyst",

        "market_researcher":
        "market_researcher",

        "data_scientist":
        "data_scientist",

        "solution_architect":
        "solution_architect",

        "financial_analyst":
        "financial_analyst",

        "reviewer":
        "reviewer",

        "FINISH":
        END
    }
)

builder.add_edge(
    "business_analyst",
    "supervisor"
)

builder.add_edge(
    "market_researcher",
    "supervisor"
)

builder.add_edge(
    "data_scientist",
    "supervisor"
)

builder.add_edge(
    "merge_analysis",
    "supervisor"
)

builder.add_edge(
    "solution_architect",
    "supervisor"
)

builder.add_edge(
    "financial_analyst",
    "supervisor"
)

builder.add_edge(
    "reviewer",
    "supervisor"
)

graph = builder.compile()