from langchain_core.messages import AIMessage

from graph.state import ConsultingState

from llm.router import invoke_llm

from prompts.market_prompt import MARKET_PROMPT

from utils.logger import logger

logger.info("Market Researcher Agent Started")

def market_researcher(
    state: ConsultingState
):

    print("\n========== Market Researcher ==========")

    response: AIMessage = invoke_llm(

        MARKET_PROMPT.format(

            user_query=state["user_query"]

        )

    )

    if response.tool_calls:

        print("\nTool Calls")

        print(response.tool_calls)

    else:

        print("\nNo Tool Called")

    return {

        "market_analysis": response.content,

        "analysis_sections": [

            f"""
    MARKET RESEARCH

    {response.content}
    """

        ]

    }