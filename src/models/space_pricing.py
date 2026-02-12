from datetime import datetime
from typing import TYPE_CHECKING
from src.models.basemodel import Basemodel, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime, Enum
from src.enums.enums import SpacePriceType


if TYPE_CHECKING:
    from src.models.space import Space


class SpacePricing(Basemodel, Base):
    __tablename__ = "space_pricings"
    space_id: Mapped[str] = mapped_column(
        ForeignKey("spaces.id"), nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    start_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    price_type: Mapped[SpacePriceType] = mapped_column(
        Enum(SpacePriceType), nullable=False
    )
    currency: Mapped[str] = mapped_column(nullable=False, default="NGN")

    space: Mapped["Space"] = relationship(back_populates="pricings")
