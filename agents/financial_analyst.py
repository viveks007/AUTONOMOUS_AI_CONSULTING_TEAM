from graph.state import ConsultingState
from llm.router import invoke_llm
from prompts.finance_prompt import FINANCE_PROMPT


def financial_analyst(
    state: ConsultingState
):
    print("========== Financial Analyst ==========")

    response = invoke_llm(
        FINANCE_PROMPT.format(
            architecture=
            state["architecture"]
        )
    )
    return {
        "roi_analysis": response.content
            }