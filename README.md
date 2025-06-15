Agentic Workflow Implementation using LangGraph

This project demonstrates a fully agentic AI workflow using LangGraph and LangChain. The workflow includes task planning, execution with tool use, feedback loops, and reinforcement learning-based retrieval — all integrated into a single dynamic pipeline.


Features:

- Agent Node Pipeline with LangGraph
- Feedback Loops with Human-in-the-Loop
- ToolAgent integration for custom tools
- Content Versioning with ChromaDB
- Reinforcement Learning-based Retrieval (RL-RAG)



Folder Structure

agentic_workflow/
├── agents/
│ ├── plan_agent.py                                   # Breaks user query into subtasks
│ ├── tool_agent.py                                   # Solves each subtask
│ ├── reflection_agent.py                             # Optionally refines tasks
│
├── tools/
│ ├── search_tool.py                                  # Simulated search tool
│ └── math_tool.py                                    # Simple calculator tool
│
├── langgraph_workflow.py                             # Main file that runs the workflow
├── requirements.txt
└── README.md



Installation:

1. Clone the repository:
   git clone https://github.com/NikhithaMaradana/Agentic-Workflow-Implementation-using-Langgraph.git
   cd Agentic-Workflow-Implementation-using-Langgraph
   
2. Install dependencies
pip install -r requirements.txt



Usage:

To run the workflow and test queries:
python langgraph_workflow.py



Enter a query:

Plan a budget trip to Japan


