from sqlalchemy.orm import Session

from app.models import Beneficiary, Case, Volunteer, WorkflowEvent


def record_event(
    db: Session,
    *,
    entity_type: str,
    entity_id: int,
    action: str,
    actor: str | None = None,
    details: str | None = None,
    related_case_id: int | None = None,
) -> WorkflowEvent:
    event = WorkflowEvent(
        entity_type=entity_type,
        entity_id=entity_id,
        action=action,
        actor=actor,
        details=details,
        related_case_id=related_case_id,
    )
    db.add(event)
    db.flush()
    return event


def advance_beneficiary_stage(
    db: Session,
    beneficiary: Beneficiary,
    new_stage: str,
    actor: str | None,
    details: str | None,
) -> Beneficiary:
    beneficiary.workflow_stage = new_stage
    record_event(
        db,
        entity_type="beneficiary",
        entity_id=beneficiary.id,
        action=f"beneficiary_stage:{new_stage}",
        actor=actor,
        details=details,
    )
    db.commit()
    db.refresh(beneficiary)
    return beneficiary


def update_volunteer_status(
    db: Session,
    volunteer: Volunteer,
    onboarding_status: str | None,
    availability_status: str | None,
    actor: str | None,
    details: str | None,
) -> Volunteer:
    if onboarding_status:
        volunteer.onboarding_status = onboarding_status
    if availability_status:
        volunteer.availability_status = availability_status

    record_event(
        db,
        entity_type="volunteer",
        entity_id=volunteer.id,
        action="volunteer_status_updated",
        actor=actor,
        details=details,
    )
    db.commit()
    db.refresh(volunteer)
    return volunteer


def assign_case_to_volunteer(
    db: Session,
    case: Case,
    volunteer: Volunteer,
    actor: str | None,
) -> Case:
    case.assigned_volunteer_id = volunteer.id
    case.stage = "assigned"
    record_event(
        db,
        entity_type="case",
        entity_id=case.id,
        action="case_assigned",
        actor=actor,
        details=f"Assigned to volunteer {volunteer.volunteer_code}",
        related_case_id=case.id,
    )
    db.commit()
    db.refresh(case)
    return case
