from typing_extensions import TypedDict, Annotated
import operator

from typing import Annotated

from langgraph.graph.message import add_messages
from langchain_core.messages import AnyMessage

class ConsultingState(TypedDict, total=False):

    user_query: str

    messages: Annotated[
    list[AnyMessage],
    add_messages
    ]

    business_analysis: str

    market_analysis: str

    ds_analysis: str

    analysis_sections: Annotated[
        list[str],
        operator.add
    ]

    architecture: str

    roi_analysis: str

    review_feedback: str

    approved: bool

    