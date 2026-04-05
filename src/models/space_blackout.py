from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime, Text
from typing import TYPE_CHECKING
from src.models.basemodel import Basemodel, Base


if TYPE_CHECKING:
    from src.models.space import Space


class SpaceBlackout(Basemodel, Base):
    __tablename__ = "space_blackouts"

    space_id: Mapped[str] = mapped_column(ForeignKey("spaces.id"))
    start_datetime: Mapped[datetime] = mapped_column(DateTime)
    end_datetime: Mapped[datetime] = mapped_column(DateTime)
    reason: Mapped[str] = mapped_column(Text, nullable=False)


    space: Mapped["Space"] = relationship(back_populates="blackouts")
