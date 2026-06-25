from typing import TypedDict, List
from typing_extensions import Annotated

class ConsultingState(TypedDict):

    user_query: str

    plan: str

    business_analysis: str

    market_analysis: str

    ds_analysis: str

    architecture: str

    roi_analysis: str

    review_feedback: str

    final_report: str

    next_agent: str

    approved: bool

    messages: List[str]