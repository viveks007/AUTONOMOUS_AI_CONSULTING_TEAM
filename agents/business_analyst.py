from graph.state import ConsultingState
from llm.groq_client import llm
from prompts.business_prompt import BUSINESS_PROMPT


def business_analyst(
    state: ConsultingState
):
    print("\n========== Business Analyst ==========")

    query = state["user_query"]

    response = llm.invoke(
        BUSINESS_PROMPT.format(
            query=query
        )
    )

    return {

    "business_analysis":
    response.content,

    "analysis_sections": [

        f"""
    BUSINESS ANALYSIS

    {response.content}
    """
        ]
    }