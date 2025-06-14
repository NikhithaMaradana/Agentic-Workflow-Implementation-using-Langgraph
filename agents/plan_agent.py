def plan_agent(state):
    query = state["query"]
    subtasks = []

    if "app" in query:
        subtasks = ["Design the UI/UX", "Plan features", "Set up backend"]
    elif "trip" in query:
        subtasks = ["Choose destinations", "Plan itinerary", "Estimate costs"]
    else:
        subtasks = ["Understand the query", "Break it into parts"]

    return {"query": query, "subtasks": subtasks, "results": [], "step": 0}
