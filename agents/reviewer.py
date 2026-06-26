from graph import state
from graph.state import ConsultingState
from llm.router import invoke_llm
from prompts.reviewer_prompt import REVIEWER_PROMPT


def reviewer(
    state: ConsultingState
):
    print("========== Reviewer ==========")

    print("\n===== Reviewer State =====")

    for key, value in state.items():
        print(key)

    response = invoke_llm(
        REVIEWER_PROMPT.format(
            business_analysis=
            state["business_analysis"],

            market_analysis=
            state["market_analysis"],

            ds_analysis=
            state["ds_analysis"],

            architecture=
            state["architecture"],

            roi_analysis=
            state["roi_analysis"]
        )
    )

    return {
        "review_feedback":
        response.content
    }