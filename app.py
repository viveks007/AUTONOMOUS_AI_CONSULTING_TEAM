from graph.workflow import graph

initial_state = {
    "user_query": """
A telecom company is facing high customer churn.
Suggest a complete AI solution.
"""
}

result = graph.invoke(initial_state)

print("\n========== FINAL OUTPUT ==========\n")

for key, value in result.items():
    print(f"\n{'='*80}")
    print(key.upper())
    print('='*80)
    print(value)