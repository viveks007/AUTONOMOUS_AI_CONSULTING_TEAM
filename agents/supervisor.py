from graph.state import ConsultingState
from utils.logger import logger

logger.info("Supervisor Loaded")


def supervisor(
    state: ConsultingState
):

    print("\n========== Supervisor ==========")

    workflow = state.get("workflow", "consulting")

    completed = set(
        state.get(
            "completed_agents",
            []
        )
    )

    # -----------------------------------
    # TOOL WORKFLOW
    # -----------------------------------

    if workflow == "tool":

        if "tool_agent" not in completed:
            next_agent = "tool_agent"
        else:
            next_agent = "end"

    # -----------------------------------
    # BUSINESS WORKFLOW
    # -----------------------------------

    elif workflow == "business":

        if "business_analyst" not in completed:
            next_agent = "business_analyst"
        else:
            next_agent = "end"

    # -----------------------------------
    # DATA SCIENCE WORKFLOW
    # -----------------------------------

    elif workflow == "datascience":

        if "data_scientist" not in completed:
            next_agent = "data_scientist"
        else:
            next_agent = "end"

    # -----------------------------------
    # CONSULTING WORKFLOW
    # -----------------------------------

    else:

        if "business_analyst" not in completed:

            next_agent = "business_analyst"

        elif "market_researcher" not in completed:

            next_agent = "market_researcher"

        elif "data_scientist" not in completed:

            next_agent = "data_scientist"

        elif "solution_architect" not in completed:

            next_agent = "solution_architect"

        elif "financial_analyst" not in completed:

            next_agent = "financial_analyst"

        elif "reviewer" not in completed:

            next_agent = "reviewer"

        else:

            next_agent = "end"

    print(f"Workflow      : {workflow}")
    print(f"Completed     : {completed}")
    print(f"Next Agent    : {next_agent}")

    return {

        "current_agent": next_agent

    }