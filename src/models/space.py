from models.base import Basemodel, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from enums.enums import DaysOfTheWeek
from typing import Optional
from models.association import space_amenity_link

class Space(Basemodel, Base):
    __tablename__ = "spaces"

    location_id: Mapped[Optional[str]] = mapped_column(ForeignKey("locations.id"), nullable=False)
    


    location: Mapped[Optional["Location"]] = relationship( back_populates="space")
    amenities: Mapped[Optional["Amenities"]] = relationship(secondary=space_amenity_link, back_populates="spaces", lazy="selectin")
    review:Mapped[Optional["Review"]] = relationship(back_populates="space")
    