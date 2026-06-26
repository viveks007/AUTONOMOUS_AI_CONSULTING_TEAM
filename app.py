from graph.workflow import graph
from langchain_core.messages import HumanMessage

query = """
A company invested ₹1,000,000.

Revenue after one year is ₹1,350,000.

Calculate ROI and explain whether the investment was successful.

Note: output token not more than 50 words
"""

initial_state = {
    "user_query": query,
"messages": [

        HumanMessage(
            content=query
        )

    ]
}

result = graph.invoke(initial_state)

print("\n========== FINAL OUTPUT ==========\n")

for key, value in result.items():
    print(f"\n{'='*80}")
    print(key.upper())
    print('='*80)
    print(value)