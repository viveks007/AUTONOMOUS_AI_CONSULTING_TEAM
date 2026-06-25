from graph.state import ConsultingState


def merge_analysis(
    state: ConsultingState
):

    print("\n========== Merge Analysis ==========")

    combined = f"""
==================================================
BUSINESS ANALYSIS
==================================================

{state.get("business_analysis","")}

==================================================
MARKET ANALYSIS
==================================================

{state.get("market_analysis","")}

==================================================
DATA SCIENCE ANALYSIS
==================================================

{state.get("ds_analysis","")}
"""

    return {
        "combined_analysis": combined
    }