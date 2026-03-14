from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import Beneficiary
from app.schemas.beneficiary import BeneficiaryCreate, BeneficiaryRead, BeneficiaryStageUpdate
from app.services.workflow import advance_beneficiary_stage, record_event

router = APIRouter(prefix="/beneficiaries", tags=["beneficiaries"])


@router.get("", response_model=list[BeneficiaryRead])
def list_beneficiaries(db: Session = Depends(get_db)):
    stmt = select(Beneficiary).order_by(Beneficiary.id.desc())
    return db.scalars(stmt).all()


@router.post("", response_model=BeneficiaryRead, status_code=201)
def create_beneficiary(payload: BeneficiaryCreate, db: Session = Depends(get_db)):
    obj = Beneficiary(**payload.model_dump())
    db.add(obj)
    db.flush()
    record_event(
        db,
        entity_type="beneficiary",
        entity_id=obj.id,
        action="beneficiary_created",
        details="Initial intake completed",
    )
    db.commit()
    db.refresh(obj)
    return obj


@router.post("/{beneficiary_id}/stage", response_model=BeneficiaryRead)
def move_beneficiary_stage(beneficiary_id: int, payload: BeneficiaryStageUpdate, db: Session = Depends(get_db)):
    beneficiary = db.get(Beneficiary, beneficiary_id)
    if not beneficiary:
        raise HTTPException(status_code=404, detail="Beneficiary not found")

    return advance_beneficiary_stage(db, beneficiary, payload.workflow_stage, payload.actor, payload.details)
