from models.base import Basemodel, Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional

class Review(Basemodel, Base):
    __tablename__ ="reviews"

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
    booking_id: Mapped[str] = mapped_column(ForeignKey("bookings.id"), nullable=False, unique=True)
    space_id: Mapped[str] = mapped_column(ForeignKey("spaces.id"), nullable=False)

    comment: Mapped[str] = mapped_column(nullable=False)


    user: Mapped[Optional["User"]] = relationship(back_populates="review")
    booking: Mapped[Optional["Booking"]] = relationship(back_populates="review")
    space: Mapped[Optional["Space"]] = relationship(back_populates="review")