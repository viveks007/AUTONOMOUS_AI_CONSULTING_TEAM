from graph.workflow import graph

initial_state = {
    "user_query": "How can telecom companies reduce customer churn in 50 words?"
}

result = graph.invoke(
    initial_state
)

print(result)