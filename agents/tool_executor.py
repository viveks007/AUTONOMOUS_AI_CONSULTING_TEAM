from langchain_core.messages import ToolMessage

from tools.tool_registry import tools_dict


def execute_tools(ai_message):

    tool_messages = []

    for tool_call in ai_message.tool_calls:

        tool_name = tool_call["name"]

        tool_args = tool_call["args"]

        tool = tools_dict.get(tool_name)

        if tool is None:

            tool_messages.append(

                ToolMessage(

                    content=f"Tool {tool_name} not found.",

                    tool_call_id=tool_call["id"]

                )

            )

            continue

        try:

            result = tool.invoke(tool_args)

        except Exception as e:

            result = f"Tool Error: {str(e)}"

        tool_messages.append(

            ToolMessage(

                content=str(result),

                tool_call_id=tool_call["id"]

            )

        )

    return tool_messages