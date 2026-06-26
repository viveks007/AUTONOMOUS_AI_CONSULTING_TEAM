from graph.state import ConsultingState
from langchain_core.messages import AIMessage
from langchain_core.messages import HumanMessage

from llm.router import invoke_llm
from prompts.business_prompt import BUSINESS_PROMPT

from utils.tool_executor import execute_tools

from utils.logger import logger

logger.info("Business Agent Started")


def business_analyst(state: ConsultingState):

    print("\n========== Business Analyst ==========")

    messages = [

            HumanMessage(

                content=BUSINESS_PROMPT.format(
                    user_query=state["user_query"]
                )

            )

        ]

    ai_message = invoke_llm(messages)

    messages.append(ai_message)

    if ai_message.tool_calls:

            tool_messages = execute_tools(ai_message)

            messages.extend(tool_messages)

            final_response = invoke_llm(messages)

    else:

            final_response = ai_message

    return {

            "business_analysis": final_response.content,

            "analysis_sections": [

                f"""
        BUSINESS ANALYSIS

        {final_response.content}
        """

            ]
        }