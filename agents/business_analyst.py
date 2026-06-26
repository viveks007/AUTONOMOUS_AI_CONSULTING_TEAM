from graph.state import ConsultingState

from prompts.business_prompt import BUSINESS_PROMPT

from agents.agent_executor import execute_agent

from utils.logger import logger

logger.info("Business Analyst Loaded")


def business_analyst(
    state: ConsultingState
):

    print("\n========== Business Analyst ==========")

    response = execute_agent(

        system_prompt=BUSINESS_PROMPT,

        user_query=state["user_query"]

    )

    completed = list(

        set(

            state.get(
                "completed_agents",
                []
            )
            + ["business_analyst"]

        )

    )

    return {

        "business_analysis": response,

        "completed_agents": completed

    }