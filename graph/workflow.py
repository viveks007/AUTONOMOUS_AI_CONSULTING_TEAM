from langgraph.graph import (
    StateGraph,
    START,
    END
)

from graph.state import ConsultingState

# Agents
from agents.intent_router import intent_router
from agents.supervisor import supervisor

from agents.tool_agent import tool_agent
from agents.business_analyst import business_analyst
from agents.market_researcher import market_researcher
from agents.data_scientist import data_scientist
from agents.solution_architect import solution_architect
from agents.financial_analyst import financial_analyst
from agents.reviewer import reviewer

# Router
from graph.supervisor_router import supervisor_router

# Checkpointer
from checkpoint.sqlite_checkpoint import checkpointer


builder = StateGraph(ConsultingState)

# ====================================================
# Nodes
# ====================================================

builder.add_node(
    "intent_router",
    intent_router
)

builder.add_node(
    "supervisor",
    supervisor
)

builder.add_node(
    "tool_agent",
    tool_agent
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

# ====================================================
# Entry
# ====================================================

builder.add_edge(
    START,
    "intent_router"
)

builder.add_edge(
    "intent_router",
    "supervisor"
)

# ====================================================
# Supervisor decides next agent
# ====================================================

builder.add_conditional_edges(

    "supervisor",

    supervisor_router,

    {

        "tool_agent": "tool_agent",

        "business_analyst": "business_analyst",

        "market_researcher": "market_researcher",

        "data_scientist": "data_scientist",

        "solution_architect": "solution_architect",

        "financial_analyst": "financial_analyst",

        "reviewer": "reviewer",

        "end": END

    }

)

# ====================================================
# Every Agent Returns to Supervisor
# ====================================================

builder.add_edge(

    "tool_agent",

    "supervisor"

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

# ====================================================
# Compile
# ====================================================

graph = builder.compile(

    checkpointer=checkpointer

)