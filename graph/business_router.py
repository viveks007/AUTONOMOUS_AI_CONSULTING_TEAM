from graph.state import ConsultingState


def business_router(
    state: ConsultingState
):

    return state["workflow"]