from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

from llm.router import invoke_llm
from utils.tool_executor import execute_tools


def execute_agent(
    system_prompt: str,
    user_query: str,
    use_tools: bool = False
):

    messages = [

        SystemMessage(
            content=system_prompt
        ),

        HumanMessage(
            content=user_query
        )

    ]

    # -----------------------------
    # First LLM Call
    # -----------------------------

    response: AIMessage = invoke_llm(

        messages,

        use_tools=use_tools

    )

    print("\n========== FIRST LLM ==========")
    print("Content :", repr(response.content))
    print("Tool Calls :", response.tool_calls)

    # -----------------------------
    # Tool Calling
    # -----------------------------

    if use_tools and response.tool_calls:

        messages.append(response)

        tool_messages = execute_tools(response)

        messages.extend(tool_messages)

        response = invoke_llm(

            messages,

            use_tools=True

        )

        print("\n========== SECOND LLM ==========")
        print("Content :", repr(response.content))
        print("Tool Calls :", response.tool_calls)

    return response.content