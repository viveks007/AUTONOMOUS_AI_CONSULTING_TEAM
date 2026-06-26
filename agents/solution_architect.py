from graph.state import ConsultingState
from llm.router import invoke_llm
from prompts.architect_prompt import ARCHITECT_PROMPT


def solution_architect(
    state: ConsultingState
):
    print("========== Solution Architect ==========")

    response = invoke_llm(
        ARCHITECT_PROMPT.format(
            analysis_sections="\n\n".join(
            state["analysis_sections"]
        ))
    )

    return {
        "architecture":
        response.content
    }