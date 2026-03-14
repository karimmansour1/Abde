from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Case(Base):
    __tablename__ = "cases"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    case_code: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    beneficiary_id: Mapped[int] = mapped_column(ForeignKey("beneficiaries.id"), nullable=False, index=True)
    assigned_volunteer_id: Mapped[int | None] = mapped_column(ForeignKey("volunteers.id"), nullable=True, index=True)
    category: Mapped[str] = mapped_column(String(50), default="general_support")
    priority: Mapped[str] = mapped_column(String(20), default="medium")
    stage: Mapped[str] = mapped_column(String(30), default="new")
    summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
