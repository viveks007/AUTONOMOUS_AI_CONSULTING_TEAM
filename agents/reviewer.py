from graph.state import ConsultingState

from prompts.reviewer_prompt import REVIEWER_PROMPT

from agents.agent_executor import execute_agent

from utils.logger import logger

logger.info("Reviewer Loaded")


def reviewer(
    state: ConsultingState
):

    print("\n========== Reviewer ==========")

    review_input = f"""

User Query
----------
{state["user_query"]}

Business Analysis
-----------------
{state.get("business_analysis", "")}

Market Analysis
---------------
{state.get("market_analysis", "")}

Data Science Analysis
---------------------
{state.get("ds_analysis", "")}

Solution Architecture
---------------------
{state.get("architecture", "")}

Financial Analysis
------------------
{state.get("roi_analysis", "")}

"""

    response = execute_agent(

        system_prompt=REVIEWER_PROMPT,

        user_query=review_input

    )

    completed = list(

        set(

            state.get(
                "completed_agents",
                []
            )
            + ["reviewer"]

        )

    )

    return {

        "review_feedback": response,

        "completed_agents": completed

    }