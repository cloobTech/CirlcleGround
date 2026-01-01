from sqlalchemy import ForeignKey, Table, Column
from models.base import Basemodel,Base
from sqlalchemy.orm import mapped_column, Mapped, relationship


class SpaceAmenity(Basemodel,Base):
    __tablename__="space_amenities"

    space_id: Mapped[str] = mapped_column(ForeignKey("spaces.id"))
    amenity_id: Mapped[str] = mapped_column(ForeignKey("amenities.id"))


    spaces: Mapped["Space"] = relationship(back_populates="space_amenities")
    amenities: Mapped["Amenity"] = relationship(back_populates="space_amenities")