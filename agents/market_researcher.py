from graph.state import ConsultingState
from llm.groq_client import llm
from prompts.market_prompt import MARKET_PROMPT


def market_researcher(
    state: ConsultingState
):
    print("========== Market Researcher ==========")

    response = llm.invoke(
        MARKET_PROMPT.format(
            user_query=state["user_query"]
        )
    )

    return {
            "market_analysis": response.content,
            "analysis_sections": [
                f"MARKET\n{response.content}"
            ]
        }