from typing import TYPE_CHECKING
from src.models.basemodel import Basemodel, Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey


if TYPE_CHECKING:
    from src.models.space import Space


class CustomAmenity(Base, Basemodel):
    __tablename__ = "custom_amenities"
    name: Mapped[str] = mapped_column(nullable=False)
    space_id: Mapped[str] = mapped_column(ForeignKey("spaces.id"))

    
    space: Mapped["Space"] = relationship(back_populates="custom_amenities")
