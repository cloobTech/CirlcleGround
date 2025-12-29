from models.base import Basemodel, Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey
from typing import Optional
from models.association import space_amenity_link


class Amenity(Basemodel, Base):
    __tablename__ = "amenities"
    name: Mapped[str] = mapped_column()


    spaces= relationship("Space", secondary=space_amenity_link, back_populates="amenities", lazy="selectin")