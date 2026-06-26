from graph.state import ConsultingState


def supervisor_router(
    state: ConsultingState
):

    return state["current_agent"]