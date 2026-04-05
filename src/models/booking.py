from datetime import datetime
from typing import TYPE_CHECKING
from src.models.basemodel import Basemodel, Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, Enum, DateTime
from src.enums.enums import BookingStatus, BookingPaymentStatus


if TYPE_CHECKING:
    from src.models.user import User
    from src.models.reviews import Review
    # from src.models.payments import Payment
    from src.models.space import Space
    from src.models.booking_history import BookingStatusHistory
    from src.models.booking_addon import BookingAddon


class Booking(Basemodel, Base):
    __tablename__ = "bookings"
    guest_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    space_id: Mapped[str] = mapped_column(ForeignKey("spaces.id"))
    status: Mapped[BookingStatus] = mapped_column(
        Enum(BookingStatus), default=BookingStatus.PENDING)
    start_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    cancelled_time: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    currency: Mapped[str] = mapped_column(nullable=False, default="NGN")
    total_price: Mapped[float] = mapped_column(nullable=False)
    payment_status: Mapped[BookingPaymentStatus] = mapped_column(
        Enum(BookingPaymentStatus), default=BookingPaymentStatus.UNPAID
    )

    # relationships
    user: Mapped["User"] = relationship(
        back_populates="bookings", uselist=False)

    space: Mapped["Space"] = relationship(back_populates="bookings")

    history_status: Mapped[list["BookingStatusHistory"]] = relationship(
        back_populates="booking",
        cascade="all, delete-orphan"

    )
    

    reviews: Mapped[list["Review"]] = relationship(
    back_populates="booking", cascade="all, delete-orphan")

    # booking_addons: Mapped[list["BookingAddon"]] = relationship(
    #     back_populates="booking",
    # )

    # payment: Mapped["Payment"] = relationship(
    #     back_populates="booking", )
    # review:Mapped["Review"] = relationship(back_populates="booking", uselist=False)
