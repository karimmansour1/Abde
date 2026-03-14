from datetime import date, datetime

from sqlalchemy import Date, DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Beneficiary(Base):
    __tablename__ = "beneficiaries"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    registration_code: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    phone: Mapped[str | None] = mapped_column(String(30), nullable=True)
    location: Mapped[str | None] = mapped_column(String(120), nullable=True)
    household_size: Mapped[int] = mapped_column(default=1)
    date_of_birth: Mapped[date | None] = mapped_column(Date, nullable=True)
    vulnerability_status: Mapped[str] = mapped_column(String(50), default="unknown")
    consent_status: Mapped[str] = mapped_column(String(30), default="pending")
    workflow_stage: Mapped[str] = mapped_column(String(30), default="intake")
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
