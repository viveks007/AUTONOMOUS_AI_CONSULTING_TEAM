from graph.state import ConsultingState

from prompts.finance_prompt import FINANCE_PROMPT

from agents.agent_executor import execute_agent

from utils.logger import logger

logger.info("Financial Analyst Loaded")


def financial_analyst(
    state: ConsultingState
):

    print("\n========== Financial Analyst ==========")

    response = execute_agent(

        system_prompt=FINANCE_PROMPT,

        user_query=state["user_query"],

        use_tools=False

    )

    completed = list(

        set(

            state.get(
                "completed_agents",
                []
            )
            + ["financial_analyst"]

        )

    )

    return {

        "roi_analysis": response,

        "completed_agents": completed

    }