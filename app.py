from graph.workflow import graph

initial_state = {
    "user_query": "How can telecom companies reduce customer churn?"
}

result = graph.invoke(
    initial_state
)

print(result)