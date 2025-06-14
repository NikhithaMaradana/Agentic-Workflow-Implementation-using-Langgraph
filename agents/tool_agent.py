from tools.search_tool import search
from tools.math_tool import calculate

def tool_agent(state):
    subtasks = state["subtasks"]
    results = state["results"]
    step = state["step"]

    if step >= len(subtasks):
        return {"results": results, "needs_reflection": False}

    current_task = subtasks[step]

    if "cost" in current_task:
        output = calculate("1000 + 2500")
    else:
        output = search(current_task)

    results.append({current_task: output})

    return {
        "subtasks": subtasks,
        "results": results,
        "step": step + 1,
        "needs_reflection": step + 1 < len(subtasks)
    }
