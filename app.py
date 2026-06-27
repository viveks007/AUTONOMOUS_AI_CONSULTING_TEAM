from graph.workflow import graph

config = {

    "configurable": {

        "thread_id": "consulting_xcvzi"

    }

}

while True:

    query = input("\nYou : ")

    if query.lower() == "exit":

        break

    result = graph.invoke(

        {

            "user_query": query,

            "completed_agents": []

        },

        config=config

    )

    print("\n========== FINAL OUTPUT ==========\n")

    if result.get("tool_response"):

        print(result["tool_response"])

    elif result.get("review_feedback"):

        print(result["review_feedback"])

    elif result.get("business_analysis"):

        print(result["business_analysis"])

    elif result.get("ds_analysis"):

        print(result["ds_analysis"])

    else:

        print(result)