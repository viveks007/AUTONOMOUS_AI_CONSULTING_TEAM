from langchain_core.messages import ToolMessage

from tools.tool_registry import TOOL_MAP


def execute_tools(ai_message):

    tool_messages = []

    for tool_call in ai_message.tool_calls:

        tool = TOOL_MAP[tool_call["name"]]

        result = tool.invoke(tool_call["args"])

        tool_messages.append(

            ToolMessage(

                content=str(result),

                tool_call_id=tool_call["id"]

            )

        )

    return tool_messages