from src.models.basemodel import Basemodel, Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.models.user import User
    from src.models.space import Space



class Review(Basemodel, Base):
    __tablename__ ="reviews"

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
    # booking_id: Mapped[str] = mapped_column(ForeignKey("bookings.id"), nullable=False)
    space_id: Mapped[str] = mapped_column(ForeignKey("spaces.id"), nullable=False)

    comment: Mapped[str] = mapped_column(nullable=False)
    is_deleted: Mapped[bool] = mapped_column(default=False)
    


    user: Mapped["User"] = relationship(back_populates="reviews")
    # booking: Mapped["Booking"] = relationship(back_populates="review")
    space: Mapped["Space"] = relationship(back_populates="reviews")