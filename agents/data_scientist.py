from langchain_core.messages import AIMessage

from graph.state import ConsultingState

from llm.groq_client import llm_with_tools

from prompts.ds_prompt import DS_PROMPT


def data_scientist(
    state: ConsultingState
):

    print("\n========== Data Scientist ==========")

    response: AIMessage = llm_with_tools.invoke(

        DS_PROMPT.format(

            user_query=state["user_query"]

        )

    )

    if response.tool_calls:

        print("\nTool Calls")

        print(response.tool_calls)

    else:

        print("\nNo Tool Called")

    return {

        "ds_analysis": response.content,

        "analysis_sections": [

            f"""
DATA SCIENCE

{response.content}
"""

        ]

    }