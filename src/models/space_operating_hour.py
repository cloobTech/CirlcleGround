from datetime import time
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Time
from typing import TYPE_CHECKING
from src.models.basemodel import Basemodel, Base


if TYPE_CHECKING:
    from src.models.space import Space


class SpaceOperatingHour(Basemodel, Base):
    __tablename__ = "space_operating_hours"
    space_id: Mapped[str] = mapped_column(ForeignKey("spaces.id"))
    open_time: Mapped[time] = mapped_column(Time, nullable=True)
    close_time: Mapped[time] = mapped_column(Time, nullable=True)
    day_of_week: Mapped[int] = mapped_column(nullable=False)
    is_closed: Mapped[bool] = mapped_column(
        nullable=False, default=False
    )

    space: Mapped["Space"] = relationship(back_populates="operating_hours")

