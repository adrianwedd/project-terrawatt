from typing import TypedDict, List, Dict, Optional

class EntityState(TypedDict, total=False):
    name: str
    status: str
    budget_allocated: float
    budget_spent: float
    risks: List[str]

class ProjectState(TypedDict, total=False):
    # Core workflow state
    messages: List[str]
    current_workstream: str
    active_agent: str
    task_queue: List[str]

    # Shared Context Layer
    regional_constraints: Dict
    financial_assumptions: Dict
    legal_framework: Dict
    temporal_roadmap: Dict

    # Entity-specific states
    landhold_co: EntityState
    build_co: EntityState
    printer_co: EntityState

    # Deliverables
    master_plan: Optional[str]
    financial_model: Optional[str]
    compliance_report: Optional[str]

    # Temporary field for demo document
    document: str
