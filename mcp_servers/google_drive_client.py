import asyncio

from mcp_servers.client import MCPClient


client = MCPClient(

    command="npx",

    args=[

        "@piotr-agier/google-drive-mcp"

    ]

)


async def discover_tools():
    tools = await client.list_tools()

    for tool in tools.tools:
        print("=" * 80)
        print(tool.name)
        print(tool.description)
        print(tool.inputSchema)


if __name__ == "__main__":

    tools = asyncio.run(
        list_google_drive_tools()
    )

    print(tools)