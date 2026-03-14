from datetime import date, datetime

from pydantic import BaseModel


class BeneficiaryBase(BaseModel):
    first_name: str
    last_name: str
    phone: str | None = None
    location: str | None = None
    household_size: int = 1
    date_of_birth: date | None = None
    vulnerability_status: str = "unknown"
    consent_status: str = "pending"
    notes: str | None = None


class BeneficiaryCreate(BeneficiaryBase):
    registration_code: str


class BeneficiaryStageUpdate(BaseModel):
    workflow_stage: str
    actor: str | None = None
    details: str | None = None


class BeneficiaryRead(BeneficiaryBase):
    id: int
    registration_code: str
    workflow_stage: str
    created_at: datetime

    class Config:
        from_attributes = True
