from src.models.basemodel import Base, Basemodel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Enum
from typing import TYPE_CHECKING
from src.enums.enums import ImageStatus

if TYPE_CHECKING:
    from src.models.space import Space


class SpaceImage(Basemodel, Base):
    __tablename__ = "space_images"

    space_id: Mapped[str] = mapped_column(ForeignKey("spaces.id"))
    url: Mapped[str] = mapped_column(nullable=True)
    order: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[ImageStatus] = mapped_column(
        Enum(ImageStatus), nullable=False, default=ImageStatus.PENDING
    )

    space: Mapped["Space"] = relationship(back_populates="images")
