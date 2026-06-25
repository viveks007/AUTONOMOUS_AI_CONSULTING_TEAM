from graph.state import ConsultingState
from llm.groq_client import llm
from prompts.market_prompt import MARKET_PROMPT


def market_researcher(
    state: ConsultingState
):

    response = llm.invoke(
        MARKET_PROMPT.format(
            business_analysis=
            state["business_analysis"]
        )
    )

    return {
        "market_analysis":
        response.content
    }