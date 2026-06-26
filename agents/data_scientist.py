from langchain_core.messages import AIMessage

from graph.state import ConsultingState

from llm.router import invoke_llm

from prompts.ds_prompt import DS_PROMPT

from utils.logger import logger

logger.info("Data Scientist Agent Started")

def data_scientist(
    state: ConsultingState
):

    print("\n========== Data Scientist ==========")

    response: AIMessage = invoke_llm(

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