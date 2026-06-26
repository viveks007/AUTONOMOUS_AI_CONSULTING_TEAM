from graph.state import ConsultingState

from prompts.ds_prompt import DS_PROMPT

from agents.agent_executor import execute_agent

from utils.logger import logger

logger.info("Data Scientist Loaded")


def data_scientist(
    state: ConsultingState
):

    print("\n========== Data Scientist ==========")

    response = execute_agent(

        system_prompt=DS_PROMPT,

        user_query=state["user_query"]

    )

    completed = list(

        set(

            state.get(
                "completed_agents",
                []
            )
            + ["data_scientist"]

        )

    )

    return {

        "ds_analysis": response,

        "completed_agents": completed

    }