from src.models.basemodel import Basemodel, Base
from src.enums.enums import PaymentStatus
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey, Enum as SAEnum

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.models.booking import Booking




class Payment(Basemodel, Base):
    __tablename__ = "payments"

    booking_id: Mapped[str] = mapped_column(ForeignKey("bookings.id"), nullable=False)
    amount: Mapped[str] = mapped_column(nullable=False)
    payment_status: Mapped[str] = mapped_column(SAEnum(PaymentStatus), default=PaymentStatus.FAILED)
    # payment_method: Mapped[str] = mapped_column(nullable=False)



    booking: Mapped["Booking"] = relationship(back_populates="payment")
    
