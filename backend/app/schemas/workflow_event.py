from datetime import datetime

from pydantic import BaseModel


class WorkflowEventRead(BaseModel):
    id: int
    entity_type: str
    entity_id: int
    action: str
    actor: str | None = None
    details: str | None = None
    related_case_id: int | None = None
    created_at: datetime

    class Config:
        from_attributes = True
