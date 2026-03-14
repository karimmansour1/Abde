from datetime import datetime

from pydantic import BaseModel


class CaseCreate(BaseModel):
    case_code: str
    beneficiary_id: int
    category: str = "general_support"
    priority: str = "medium"
    summary: str | None = None


class CaseAssignVolunteer(BaseModel):
    volunteer_id: int
    actor: str | None = None


class CaseStageUpdate(BaseModel):
    stage: str
    actor: str | None = None
    details: str | None = None


class CaseRead(BaseModel):
    id: int
    case_code: str
    beneficiary_id: int
    assigned_volunteer_id: int | None = None
    category: str
    priority: str
    stage: str
    summary: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True
