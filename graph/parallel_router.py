from langgraph.types import Send

from graph.state import ConsultingState

def parallel_router(state: ConsultingState):

    return [


        Send(
            "market_researcher",
            state
        ),

        Send(
            "data_scientist",
            state
        )

    ]