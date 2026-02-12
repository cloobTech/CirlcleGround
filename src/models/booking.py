from datetime import datetime
from typing import TYPE_CHECKING
from src.models.basemodel import Basemodel, Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, Enum, DateTime
from src.enums.enums import BookingStatus


if TYPE_CHECKING:
    from src.models.user import User
    from src.models.payments import Payment
    from src.models.space import Space


class Booking(Basemodel, Base):
    __tablename__ = "bookings"
    guest_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    space_id: Mapped[str] = mapped_column(ForeignKey("spaces.id"))
    status: Mapped[BookingStatus] = mapped_column(
        Enum(BookingStatus), default=BookingStatus.EXPIRED)
    start_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    cancelled_time: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    currency: Mapped[str] = mapped_column(nullable=False, default="NGN")

    # relationships
    user: Mapped["User"] = relationship(
        back_populates="bookings", uselist=False)

    payment: Mapped["Payment"] = relationship(
        back_populates="booking", uselist=False, cascade="all, delete-orphan")

    space: Mapped["Space"] = relationship(back_populates="bookings")

    # review:Mapped["Review"] = relationship(back_populates="booking", uselist=False)
