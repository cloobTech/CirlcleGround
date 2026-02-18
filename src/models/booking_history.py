from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text, Enum
from typing import TYPE_CHECKING
from src.models.basemodel import Basemodel, Base
from src.enums.enums import BookingStatus


if TYPE_CHECKING:
    from src.models.booking import Booking
    from src.models.user import User


class BookingStatusHistory(Basemodel, Base):
    __tablename__ = "booking_status_histories"

    booking_id: Mapped[str] = mapped_column(ForeignKey("bookings.id"))
    changed_by_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    note: Mapped[str] = mapped_column(Text)
    status: Mapped[BookingStatus] = mapped_column(
        Enum(BookingStatus), default=BookingStatus.PENDING)
    booking: Mapped["Booking"] = relationship(
        "Booking", back_populates="history_status")
    changed_by: Mapped["User"] = relationship("User")
