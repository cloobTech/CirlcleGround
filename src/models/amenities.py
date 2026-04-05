from src.models.basemodel import Basemodel, Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.models.space_amenities import SpaceAmenity


class Amenity(Basemodel, Base):
    __tablename__ = "amenities"
    name: Mapped[str] = mapped_column(nullable=False)
    category: Mapped[str] = mapped_column(nullable=False)

    space_amenities: Mapped[list["SpaceAmenity"]] = relationship(
        back_populates="amenities",
        cascade="all, delete-orphan"
    )
