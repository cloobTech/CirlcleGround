from datetime import time
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Time
from typing import TYPE_CHECKING
from src.models.basemodel import Basemodel, Base


if TYPE_CHECKING:
    from src.models.booking import Booking


class BookingAddon(Base, Basemodel):
    __tablename__ = "booking_addons"

    # booking_id: Mapped[str] = mapped_column(
    #     ForeignKey("bookings.id", ondelete="CASCADE")
    # )
    addon_id: Mapped[str] = mapped_column(
        ForeignKey("space_addons.id", ondelete="CASCADE")
    )


    # booking: Mapped["Booking"] = relationship(
    #     "Booking", back_populates="booking_addons")
