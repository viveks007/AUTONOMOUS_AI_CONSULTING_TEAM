from graph.state import ConsultingState

from langchain_core.messages import (
    HumanMessage,
    SystemMessage
)

from llm.router import invoke_llm

from prompts.intent_prompt import INTENT_PROMPT


def intent_router(
    state: ConsultingState
):

    print("\n========== Intent Router ==========")

    messages = [

        SystemMessage(
            content=INTENT_PROMPT
        ),

        HumanMessage(
            content=state["user_query"]
        )

    ]

    response = invoke_llm(messages)

    raw_response = response.content.strip()

    print(f"LLM Response : {raw_response}")

    text = raw_response.upper()

    if "TOOL" in text:

        intent = "TOOL"

    elif "BUSINESS" in text:

        intent = "BUSINESS"

    elif "DATA" in text:

        intent = "DATA_SCIENCE"

    else:

        intent = "CONSULTING"

    workflow_mapping = {

        "TOOL": "tool",

        "BUSINESS": "business",

        "DATA_SCIENCE": "datascience",

        "CONSULTING": "consulting"

    }

    workflow = workflow_mapping[intent]

    print(f"Detected Intent : {intent}")
    print(f"Workflow        : {workflow}")

    return {

        "workflow": workflow

    }