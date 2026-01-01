from sqlalchemy.orm import mapped_column, Mapped, relationship
from models.base import Basemodel, Base
# from typing import Optional, List

class Location(Basemodel, Base):
    __tablename__ = "locations"

    city: Mapped[str] = mapped_column(nullable=False)
    state: Mapped[str] = mapped_column(nullable=False)

    
    spaces: Mapped[list["Space"]] = relationship(back_populates="location")

    