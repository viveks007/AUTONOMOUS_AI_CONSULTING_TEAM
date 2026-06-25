def supervisor_router(state):

    if not state.get(
        "business_analysis"
    ):
        return "business_analyst"

    if not state.get(
        "market_analysis"
    ):
        return "market_researcher"

    if not state.get(
        "ds_analysis"
    ):
        return "data_scientist"

    if not state.get(
        "combined_analysis"
    ):
        return "merge_analysis"

    if not state.get(
        "architecture"
    ):
        return "solution_architect"

    if not state.get(
        "roi_analysis"
    ):
        return "financial_analyst"

    if not state.get(
        "review_feedback"
    ):
        return "reviewer"

    return "FINISH"