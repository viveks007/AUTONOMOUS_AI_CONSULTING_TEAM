from graph.state import ConsultingState
from llm.groq_client import llm
from prompts.architect_prompt import ARCHITECT_PROMPT


def solution_architect(
    state: ConsultingState
):

    response = llm.invoke(
        ARCHITECT_PROMPT.format(
            business_analysis=
            state["business_analysis"],

            market_analysis=
            state["market_analysis"],

            ds_analysis=
            state["ds_analysis"]
        )
    )

    return {
        "architecture":
        response.content
    }