from typing_extensions import TypedDict, Annotated
import operator

class ConsultingState(TypedDict, total=False):

    user_query: str

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

    messages: str