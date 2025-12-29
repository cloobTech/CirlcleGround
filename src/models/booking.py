from models.base import Basemodel, Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey, Enum as SAEnum
from typing import Optional
from enums.enums import Status

class Booking(Basemodel, Base):
    __tablename__ = "bookings"
    user_id: Mapped[Optional[str]] = mapped_column(ForeignKey("users.id"))
    status: Mapped[str] = mapped_column(SAEnum(Status), default=Status.NOT_PAID)


    payment: Mapped[Optional["Payment"]] = relationship(back_populates="booking", uselist=False)

    