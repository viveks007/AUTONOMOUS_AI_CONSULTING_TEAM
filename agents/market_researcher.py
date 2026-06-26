from graph.state import ConsultingState

from langchain_core.messages import AIMessage

from llm.router import invoke_llm

from prompts.market_prompt import MARKET_PROMPT

from utils.tool_executor import execute_tools

from graph.state import ConsultingState

from langchain_core.messages import (
    AIMessage,
    HumanMessage
)

from llm.router import invoke_llm

from prompts.market_prompt import MARKET_PROMPT

from utils.tool_executor import execute_tools


def market_researcher(state: ConsultingState):

    print("\n========== Market Researcher ==========")

    messages = [

        HumanMessage(

            content=MARKET_PROMPT.format(

                user_query=state["user_query"]

            )

        )

    ]

    ai_message: AIMessage = invoke_llm(messages)

    messages.append(ai_message)

    if ai_message.tool_calls:

        print("\nTool Calls Found")
        print(ai_message.tool_calls)

        tool_messages = execute_tools(ai_message)

        messages.extend(tool_messages)

        final_response: AIMessage = invoke_llm(messages)

    else:

        print("\nNo Tool Calls")

        final_response = ai_message

    return {

        "market_analysis": final_response.content,

        "analysis_sections": [

            f"""
MARKET ANALYSIS

{final_response.content}
"""

        ]

    }