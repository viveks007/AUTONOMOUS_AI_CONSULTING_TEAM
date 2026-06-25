from graph.state import ConsultingState
from llm.groq_client import llm
from prompts.finance_prompt import FINANCE_PROMPT


def financial_analyst(
    state: ConsultingState
):

    response = llm.invoke(
        FINANCE_PROMPT.format(
            architecture=
            state["architecture"]
        )
    )

    return {
        "roi_analysis":
        response.content
    }