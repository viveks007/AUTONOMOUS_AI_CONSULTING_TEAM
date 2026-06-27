from graph.state import ConsultingState

from prompts.architect_prompt import ARCHITECT_PROMPT

from agents.agent_executor import execute_agent

from utils.logger import logger

logger.info("Solution Architect Loaded")


def solution_architect(
    state: ConsultingState
):

    print("\n========== Solution Architect ==========")

    response = execute_agent(

        system_prompt=ARCHITECT_PROMPT,

        user_query=state["user_query"],

        use_tools=False

    )

    completed = list(

        set(

            state.get(
                "completed_agents",
                []
            )
            + ["solution_architect"]

        )

    )

    return {

        "architecture": response,

        "completed_agents": completed

    }