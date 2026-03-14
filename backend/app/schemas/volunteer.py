from datetime import datetime

from pydantic import BaseModel


class VolunteerBase(BaseModel):
    first_name: str
    last_name: str
    phone: str | None = None
    email: str | None = None
    skills: str | None = None
    branch: str | None = None


class VolunteerCreate(VolunteerBase):
    volunteer_code: str


class VolunteerStatusUpdate(BaseModel):
    onboarding_status: str | None = None
    availability_status: str | None = None
    actor: str | None = None
    details: str | None = None


class VolunteerRead(VolunteerBase):
    id: int
    volunteer_code: str
    onboarding_status: str
    availability_status: str
    created_at: datetime

    class Config:
        from_attributes = True
