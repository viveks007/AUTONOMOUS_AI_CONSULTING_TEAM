from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

from llm.router import invoke_llm

from utils.tool_executor import execute_tools


def execute_agent(
    system_prompt: str,
    user_query: str
):

    messages = [

        SystemMessage(
            content=system_prompt
        ),

        HumanMessage(
            content=user_query
        )

    ]

    response: AIMessage = invoke_llm(messages)

    messages.append(response)

    # -----------------------------
    # Tool Calling
    # -----------------------------

    if response.tool_calls:

        tool_messages = execute_tools(response)

        messages.extend(tool_messages)

        response = invoke_llm(messages)

    return response.content