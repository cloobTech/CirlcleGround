from src.models.basemodel import Basemodel, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from src.enums.enums import DaysOfTheWeek
from typing import Optional

from typing import TYPE_CHECKING
# from models.association import space_amenity_link


if TYPE_CHECKING:
    from src.models.location import Location
    from src.models.reviews import Review
    from src.models.space_amenities import SpaceAmenity

    


class Space(Basemodel, Base):
    __tablename__ = "spaces"

    location_id: Mapped[str] = mapped_column(ForeignKey("locations.id"), nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[str] = mapped_column(nullable=False)
    max_guests: Mapped[str] = mapped_column(nullable=False)
    is_deleted: Mapped[bool] = mapped_column(default=False)



    location: Mapped["Location"] = relationship( back_populates="spaces")

    reviews:Mapped[list["Review"]] = relationship(back_populates="space", cascade="all, delete-orphan")

    space_amenities: Mapped[list["SpaceAmenity"]] = relationship(
        back_populates="spaces",
        cascade="all, delete-orphan"
    )
    