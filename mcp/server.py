from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "Consulting MCP Server"
)


@mcp.tool()
def swot_analysis(company: str) -> str:
    """
    Perform SWOT analysis.
    """

    return f"""
        SWOT Analysis for {company}

        Strengths:
        - Strong brand
        - Large customer base
        - Innovation

        Weaknesses:
        - High operational costs

        Opportunities:
        - Emerging markets
        - AI adoption

        Threats:
        - Competition
        - Regulations
        """

@mcp.tool()
def pestle_analysis(company: str) -> str:
    """
    Perform PESTLE analysis.
    """

    return f"""
        PESTLE Analysis for {company}

        Political
        Economic
        Social
        Technological
        Legal
        Environmental
        """

@mcp.tool()
def business_canvas(company: str) -> str:
    """
    Generate Business Model Canvas.
    """

    return f"""
        Business Model Canvas

        Company : {company}

        Key Partners

        Key Activities

        Value Proposition

        Customer Segments

        Revenue Streams
        """


if __name__ == "__main__":

    print("=" * 50)
    print("Starting Consulting MCP Server...")
    print("=" * 50)

    mcp.run()