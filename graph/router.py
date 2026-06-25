def supervisor_router(state):

    if not state.get(
        "business_analysis", ""
    ).strip():
        return "business_analyst"

    if not state.get(
        "market_analysis", ""
    ).strip():
        return "market_researcher"

    if not state.get(
        "ds_analysis", ""
    ).strip():
        return "data_scientist"

    if not state.get(
        "architecture", ""
    ).strip():
        return "solution_architect"

    if not state.get(
        "roi_analysis", ""
    ).strip():
        return "financial_analyst"

    if not state.get(
        "review_feedback", ""
    ).strip():
        return "reviewer"

    return "FINISH"