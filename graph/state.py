from typing_extensions import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import AnyMessage


class ConsultingState(TypedDict):

    user_query: str

    business_analysis: str

    market_analysis: str

    ds_analysis: str

    architecture: str

    roi_analysis: str

    review_feedback: str

    final_report: str

    approved: bool

    messages: Annotated[
        list[AnyMessage],
        add_messages
    ]