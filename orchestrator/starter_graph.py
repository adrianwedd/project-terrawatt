from __future__ import annotations

from typing import Dict

from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3

from .state import ProjectState


# --- Node Definitions -----------------------------------------------------

def ingest(state: ProjectState) -> Dict:
    """Simulate ingesting a document."""
    doc = state.get("document", "")
    messages = state.get("messages", [])
    messages.append(f"INGEST:{doc}")
    return {"messages": messages}


def analyze(state: ProjectState) -> Dict:
    """Very basic analysis step."""
    doc = state["messages"][-1].split(":", 1)[1]
    messages = state["messages"]
    messages.append(f"ANALYZED:{doc.upper()}")
    return {"messages": messages}


# --- Graph Builder -------------------------------------------------------

def build_graph(path: str = "graph_state.sqlite"):
    builder = StateGraph(ProjectState)
    builder.add_node("ingest", ingest)
    builder.add_node("analyze", analyze)
    builder.set_entry_point("ingest")
    builder.add_edge("ingest", "analyze")
    builder.add_edge("analyze", END)
    conn = sqlite3.connect(path, check_same_thread=False)
    checkpointer = SqliteSaver(conn)
    return builder.compile(checkpointer=checkpointer)


def demo_resumable_run(document: str):
    """Run the graph in two stages to demonstrate persistence."""
    session_id = "demo"
    app = build_graph()

    start_state: ProjectState = {
        "messages": [],
        "current_workstream": "demo",
        "active_agent": "ingest",
        "task_queue": [],
        "regional_constraints": {},
        "financial_assumptions": {},
        "legal_framework": {},
        "temporal_roadmap": {},
        "landhold_co": {},
        "build_co": {},
        "printer_co": {},
        "document": document,
        "master_plan": None,
        "financial_model": None,
        "compliance_report": None,
    }

    # Process first node then exit early.
    config = {"configurable": {"thread_id": session_id}}
    stream = app.stream(start_state, config=config)
    print("First event:", next(stream))
    stream.close()

    # Resume from persisted state
    print("Resuming...")
    for event in app.stream(None, config=config):
        print("Resumed event:", event)


if __name__ == "__main__":
    demo_resumable_run("hello world")
