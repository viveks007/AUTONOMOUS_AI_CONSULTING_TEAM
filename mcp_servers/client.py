from mcp.client.session import ClientSession
from mcp.client.stdio import (
    stdio_client,
    StdioServerParameters,
)


class MCPClient:

    def __init__(
        self,
        command: str,
        args: list[str],
    ):

        self.server = StdioServerParameters(
            command=command,
            args=args,
        )

    # ---------------------------------------
    # List all tools
    # ---------------------------------------

    async def list_tools(self):

        print("Connecting to MCP...")

        async with stdio_client(self.server) as (
            read_stream,
            write_stream,
        ):

            print("Connected")

            async with ClientSession(
                read_stream,
                write_stream,
            ) as session:

                print("Initializing Session...")

                await session.initialize()

                print("Session Initialized")

                tools = await session.list_tools()

                print("Tools Retrieved")

                return tools

    # ---------------------------------------
    # Call a tool
    # ---------------------------------------

    async def call_tool(
        self,
        tool_name: str,
        arguments: dict,
    ):

        print(f"\nCalling Tool : {tool_name}")

        async with stdio_client(self.server) as (
            read_stream,
            write_stream,
        ):

            async with ClientSession(
                read_stream,
                write_stream,
            ) as session:

                await session.initialize()

                result = await session.call_tool(
                    tool_name,
                    arguments,
                )

                return result