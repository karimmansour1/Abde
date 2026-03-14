from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import Beneficiary, Case, Volunteer
from app.schemas.case import CaseAssignVolunteer, CaseCreate, CaseRead, CaseStageUpdate
from app.services.workflow import assign_case_to_volunteer, record_event

router = APIRouter(prefix="/cases", tags=["cases"])


@router.get("", response_model=list[CaseRead])
def list_cases(db: Session = Depends(get_db)):
    stmt = select(Case).order_by(Case.id.desc())
    return db.scalars(stmt).all()


@router.post("", response_model=CaseRead, status_code=201)
def create_case(payload: CaseCreate, db: Session = Depends(get_db)):
    beneficiary = db.get(Beneficiary, payload.beneficiary_id)
    if not beneficiary:
        raise HTTPException(status_code=404, detail="Beneficiary not found")

    case = Case(**payload.model_dump())
    db.add(case)
    db.flush()
    record_event(
        db,
        entity_type="case",
        entity_id=case.id,
        action="case_created",
        details="Case opened from beneficiary workflow",
        related_case_id=case.id,
    )
    db.commit()
    db.refresh(case)
    return case


@router.post("/{case_id}/assign", response_model=CaseRead)
def assign_case(case_id: int, payload: CaseAssignVolunteer, db: Session = Depends(get_db)):
    case = db.get(Case, case_id)
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")

    volunteer = db.get(Volunteer, payload.volunteer_id)
    if not volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")

    return assign_case_to_volunteer(db, case, volunteer, payload.actor)


@router.post("/{case_id}/stage", response_model=CaseRead)
def update_case_stage(case_id: int, payload: CaseStageUpdate, db: Session = Depends(get_db)):
    case = db.get(Case, case_id)
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")

    case.stage = payload.stage
    record_event(
        db,
        entity_type="case",
        entity_id=case.id,
        action=f"case_stage:{payload.stage}",
        actor=payload.actor,
        details=payload.details,
        related_case_id=case.id,
    )
    db.commit()
    db.refresh(case)
    return case
