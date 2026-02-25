from sqlalchemy.orm import mapped_column, Mapped, relationship
from src.models.basemodel import Basemodel, Base
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.models.space import Space


class Location(Basemodel, Base):
    __tablename__ = "locations"

    country: Mapped[str] = mapped_column(nullable=False)
    city: Mapped[str] = mapped_column(nullable=False)
    state: Mapped[str] = mapped_column(nullable=False)
    latitude: Mapped[float] = mapped_column(nullable=False)
    longitude: Mapped[float] = mapped_column(nullable=False)
    formatted_address: Mapped[str] = mapped_column(nullable=False)
    original_address: Mapped[str] = mapped_column(nullable=False, unique=True)
    normalized_address: Mapped[str] = mapped_column(nullable=False)
    provider: Mapped[str] = mapped_column(nullable=False)

    spaces: Mapped[list["Space"]] = relationship(
        back_populates="location", cascade="all, delete-orphan")
