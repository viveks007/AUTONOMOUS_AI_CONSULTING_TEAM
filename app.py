from graph.workflow import graph
from langchain_core.messages import HumanMessage

query = """
What is today's date and current quarter?
"""

initial_state = {
    "user_query": query,
"messages": [

        HumanMessage(
            content=query
        )

    ]
}

config = {
    "configurable": {
        "thread_id": "consulting_demo_2"
    }
}

result = graph.invoke(
    initial_state,
    config=config
)

checkpoint = graph.get_state(config)

#print(checkpoint.values)

print("\n========== FINAL OUTPUT ==========\n")

for key, value in result.items():
    print(f"\n{'='*80}")
    print(key.upper())
    print('='*80)
    print(value)