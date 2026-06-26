from graph.state import ConsultingState

from prompts.market_prompt import MARKET_PROMPT

from agents.agent_executor import execute_agent

from utils.logger import logger

logger.info("Market Researcher Loaded")


def market_researcher(
    state: ConsultingState
):

    print("\n========== Market Researcher ==========")

    response = execute_agent(

        system_prompt=MARKET_PROMPT,

        user_query=state["user_query"]

    )

    completed = list(

        set(

            state.get(
                "completed_agents",
                []
            )
            + ["market_researcher"]

        )

    )

    return {

        "market_analysis": response,

        "completed_agents": completed

    }