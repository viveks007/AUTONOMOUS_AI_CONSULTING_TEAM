from langgraph.graph import StateGraph

from graph.state import ConsultingState

from agents.business_analyst import business_analyst
from agents.market_researcher import market_researcher


builder = StateGraph(
    ConsultingState
)

builder.add_node(
    "business_analyst",
    business_analyst
)

builder.add_node(
    "market_researcher",
    market_researcher
)

builder.set_entry_point(
    "business_analyst"
)

builder.add_edge(
    "business_analyst",
    "market_researcher"
)

builder.set_finish_point(
    "market_researcher"
)

graph = builder.compile()