from langgraph.types import Send

from graph.state import ConsultingState

def parallel_router(state: ConsultingState):

    return [

        Send(
            "business_analyst",
            state
        ),

        Send(
            "market_researcher",
            state
        ),

        Send(
            "data_scientist",
            state
        )

    ]