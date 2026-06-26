from graph.state import ConsultingState


def intent_router_edges(
    state: ConsultingState
):

    return state["workflow"]