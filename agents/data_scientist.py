from graph.state import ConsultingState

from langchain_core.messages import AIMessage

from llm.router import invoke_llm

from prompts.ds_prompt import DS_PROMPT

from utils.tool_executor import execute_tools

from graph.state import ConsultingState

from langchain_core.messages import (
    AIMessage,
    HumanMessage
)

from llm.router import invoke_llm

from prompts.ds_prompt import DS_PROMPT

from utils.tool_executor import execute_tools


def data_scientist(state: ConsultingState):

    print("\n========== Data Scientist ==========")

    messages = [

        HumanMessage(

            content=DS_PROMPT.format(

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

        "ds_analysis": final_response.content,

        "analysis_sections": [

            f"""
DATA SCIENCE ANALYSIS

{final_response.content}
"""

        ]

    }