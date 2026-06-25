from graph.state import ConsultingState
from llm.groq_client import llm
from prompts.ds_prompt import DS_PROMPT


def data_scientist(
    state: ConsultingState
):
    print("========== Data Scientist ==========")

    response = llm.invoke(
        DS_PROMPT.format(
            user_query = state["user_query"]
        )
    )

    return {

        "ds_analysis":
        response.content,

        "analysis_sections": [

            f"""
        DATA SCIENCE ANALYSIS

        {response.content}
        """
            ]
        }