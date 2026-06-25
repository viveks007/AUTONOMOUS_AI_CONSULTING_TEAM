from graph.state import ConsultingState
from llm.groq_client import llm
from prompts.finance_prompt import FINANCE_PROMPT


def financial_analyst(
    state: ConsultingState
):
    print("========== Financial Analyst ==========")

    response = llm.invoke(
        FINANCE_PROMPT.format(
            architecture=
            state["architecture"]
        )
    )

    return {

    "market_analysis":
    response.content,

    "analysis_sections": [

        f"""
    MARKET ANALYSIS

    {response.content}
    """
        ]
    }