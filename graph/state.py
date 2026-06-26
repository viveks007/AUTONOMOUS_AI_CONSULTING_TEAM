from typing_extensions import TypedDict


class ConsultingState(TypedDict, total=False):

    user_query: str

    workflow: str

    current_agent: str

    completed_agents: list[str]

    tool_response: str

    business_analysis: str

    market_analysis: str

    ds_analysis: str

    architecture: str

    roi_analysis: str

    review_feedback: str