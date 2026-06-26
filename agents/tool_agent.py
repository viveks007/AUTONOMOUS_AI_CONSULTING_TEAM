from graph.state import ConsultingState

from prompts.tool_prompt import TOOL_PROMPT

from agents.agent_executor import execute_agent

from utils.logger import logger

logger.info("Tool Agent Loaded")


def tool_agent(
    state: ConsultingState
):

    print("\n========== Tool Agent ==========")

    response = execute_agent(

        system_prompt=TOOL_PROMPT,

        user_query=state["user_query"]

    )

    completed = list(

        set(

            state.get(
                "completed_agents",
                []
            )
            + ["tool_agent"]

        )

    )

    return {

        "tool_response": response,

        "completed_agents": completed

    }