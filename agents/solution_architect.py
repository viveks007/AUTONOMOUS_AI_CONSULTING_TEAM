from graph.state import ConsultingState
from llm.groq_client import llm
from prompts.architect_prompt import ARCHITECT_PROMPT


def solution_architect(
    state: ConsultingState
):

    response = llm.invoke(
        ARCHITECT_PROMPT.format(
            combined_analysis=
            state["combined_analysis"]
        )
    )

    return {
        "architecture":
        response.content
    }