from graph.tool_node import tool_node


def execute_tools(state):
    return tool_node.invoke(state)