from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import Volunteer
from app.schemas.volunteer import VolunteerCreate, VolunteerRead, VolunteerStatusUpdate
from app.services.workflow import record_event, update_volunteer_status

router = APIRouter(prefix="/volunteers", tags=["volunteers"])


@router.get("", response_model=list[VolunteerRead])
def list_volunteers(db: Session = Depends(get_db)):
    stmt = select(Volunteer).order_by(Volunteer.id.desc())
    return db.scalars(stmt).all()


@router.post("", response_model=VolunteerRead, status_code=201)
def create_volunteer(payload: VolunteerCreate, db: Session = Depends(get_db)):
    volunteer = Volunteer(**payload.model_dump())
    db.add(volunteer)
    db.flush()
    record_event(
        db,
        entity_type="volunteer",
        entity_id=volunteer.id,
        action="volunteer_created",
        details="Volunteer profile created",
    )
    db.commit()
    db.refresh(volunteer)
    return volunteer


@router.post("/{volunteer_id}/status", response_model=VolunteerRead)
def patch_volunteer_status(volunteer_id: int, payload: VolunteerStatusUpdate, db: Session = Depends(get_db)):
    volunteer = db.get(Volunteer, volunteer_id)
    if not volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")

    return update_volunteer_status(
        db,
        volunteer,
        payload.onboarding_status,
        payload.availability_status,
        payload.actor,
        payload.details,
    )
