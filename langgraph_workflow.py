import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from typing import TypedDict, List, Dict, Any

class AgentState(TypedDict):
    query: str
    subtasks: List[str]
    results: List[Dict[str, Any]]
    step: int
    needs_reflection: bool



from langgraph.graph import StateGraph, END
from agents.plan_agent import plan_agent
from agents.tool_agent import tool_agent
from agents.reflection_agent import reflection_agent

def build_workflow():
    graph = graph = StateGraph(AgentState)
    graph.add_node("planner", plan_agent)
    graph.add_node("executor", tool_agent)
    graph.add_node("reflector", reflection_agent)

    graph.set_entry_point("planner")
    graph.add_edge("planner", "executor")
    graph.add_conditional_edges(
        "executor",
        lambda state: "yes" if state.get("needs_reflection") else "no",
        {"yes": "reflector", "no": END}
    )
    graph.add_edge("reflector", "executor")
    return graph.compile()


if __name__ == "__main__":
    workflow = build_workflow()
    user_query = input("Enter your query: ")
    result = workflow.invoke({"query": user_query})
    print("\nFinal Result:")
    print(result)
