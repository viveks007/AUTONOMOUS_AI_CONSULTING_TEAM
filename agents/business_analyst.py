from urllib import response

from graph.state import ConsultingState
from langchain_core.messages import AIMessage


from llm.router import invoke_llm
from prompts.business_prompt import BUSINESS_PROMPT

from utils.logger import logger

logger.info("Business Agent Started")


def business_analyst(state: ConsultingState):

    print("\n========== Business Analyst ==========")

    response: AIMessage = invoke_llm(
        BUSINESS_PROMPT.format(
            user_query=state["user_query"]
        )
    )

    if response.tool_calls:
        print("\nTool Calls Found")
        print(response.tool_calls)
    else:
        print("\nNo Tool Calls")

    return {
        "messages": [response],
        "business_analysis": response.content,
        "analysis_sections": [
            f"BUSINESS ANALYSIS\n\n{response.content}"
        ]
    }