from fastapi import APIRouter, Depends
from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import WorkflowEvent
from app.schemas.workflow_event import WorkflowEventRead

router = APIRouter(prefix="/workflows", tags=["workflows"])


@router.get("/events", response_model=list[WorkflowEventRead])
def list_workflow_events(limit: int = 100, db: Session = Depends(get_db)):
    stmt = select(WorkflowEvent).order_by(desc(WorkflowEvent.created_at)).limit(limit)
    return db.scalars(stmt).all()
