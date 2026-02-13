from src.models.basemodel import Basemodel, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.space import Space


class SpaceRule(Basemodel, Base):
    __tablename__ = "space_rules"
    space_id: Mapped[str] = mapped_column(ForeignKey("spaces.id"))
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)


    space: Mapped["Space"] = relationship(back_populates="rules")
