from graph.state import ConsultingState
from langchain_core.messages import AIMessage

from llm.groq_client import llm
from llm.groq_client import llm_with_tools
from prompts.business_prompt import BUSINESS_PROMPT


def business_analyst(state: ConsultingState):

    print("\n========== Business Analyst ==========")

    response: AIMessage = llm_with_tools.invoke(
        BUSINESS_PROMPT.format(
            user_query=state["user_query"]
        )
    )

    if response.tool_calls:
        print("\nTool Calls Found")
        print(response.tool_calls)
    else:
        print("\nNo Tool Calls")

    return {
        "business_analysis": response.content,
        "analysis_sections": [
            f"BUSINESS ANALYSIS\n\n{response.content}"
        ]
    }