def supervisor_router(state):

    print("\n===== ROUTER =====")
    print(f"Business: {bool(state.get('business_analysis'))}")
    print(f"Market: {bool(state.get('market_analysis'))}")
    print(f"DS: {bool(state.get('ds_analysis'))}")
    print(f"Combined: {bool(state.get('combined_analysis'))}")
    print(f"Architecture: {bool(state.get('architecture'))}")
    print(f"ROI: {bool(state.get('roi_analysis'))}")
    print(f"Review: {bool(state.get('review_feedback'))}")

    if not state.get("business_analysis"):
        return "business_analyst"

    if not state.get("market_analysis"):
        return "market_researcher"

    if not state.get("ds_analysis"):
        return "data_scientist"

    if not state.get("combined_analysis"):
        return "merge_analysis"

    if not state.get("architecture"):
        return "solution_architect"

    if not state.get("roi_analysis"):
        return "financial_analyst"

    if not state.get("review_feedback"):
        return "reviewer"

    return "FINISH"