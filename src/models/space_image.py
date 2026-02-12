from src.models.basemodel import Base, Basemodel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.space import Space


class SpaceImage(Basemodel, Base):
    __tablename__ = "space_images"

    space_id: Mapped[str] = mapped_column(ForeignKey("spaces.id"))
    url: Mapped[str] = mapped_column(nullable=False)
    order: Mapped[int] = mapped_column(nullable=False)

    space: Mapped["Space"] = relationship(back_populates="images")
