from models.base import Basemodel, Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey, Enum as SAEnum
from typing import Optional
from enums.enums import Status

class Booking(Basemodel, Base):
    __tablename__ = "bookings"
    guest_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    space_id: Mapped[str] = mapped_column(ForeignKey("space"))
    status: Mapped[str] = mapped_column(SAEnum(Status), default=Status.NOT_PAID)
    start_time: Mapped[str] = mapped_column()
    end_time: Mapped[str] = mapped_column()
    cancelled_time: Mapped[str] = mapped_column()
    price_id: Mapped[str] = mapped_column()


    #relationships
    user : Mapped["User"] = relationship(back_populates="booking", uselist=False)

    payment: Mapped["Payment"] = relationship(back_populates="booking", uselist=False)

    # review:Mapped["Review"] = relationship(back_populates="booking", uselist=False)

    