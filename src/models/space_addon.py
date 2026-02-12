from typing import TYPE_CHECKING
from src.models.basemodel import Basemodel, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

if TYPE_CHECKING:
    from src.models.space import Space


class SpaceAddon(Basemodel, Base):
    __tablename__ = "space_addons"

    id: Mapped[str] = mapped_column(primary_key=True)
    space_id: Mapped[str] = mapped_column(
        ForeignKey("spaces.id"), nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column(nullable=True)
    price: Mapped[float] = mapped_column(nullable=False)
    currency: Mapped[str] = mapped_column(default="NGN")

    space: Mapped['Space'] = relationship(
        back_populates="space_addons",

    )
