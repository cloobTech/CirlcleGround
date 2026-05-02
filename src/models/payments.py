from sqlalchemy.orm import mapped_column, Mapped, relationship
from uuid import uuid4
from decimal import Decimal
from sqlalchemy import ForeignKey, Enum, String, Numeric
from typing import TYPE_CHECKING
from src.models.basemodel import Basemodel, Base
from src.enums.enums import PaymentStatus, Provider, PaymentMethod





if TYPE_CHECKING:
    from src.models.booking import Booking
    from src.models.user import User




class Payment(Basemodel, Base):
    __tablename__ = "payments"

    user_id: Mapped[str] = mapped_column(ForeignKey('users.id'), nullable=False)
    booking_id: Mapped[str] = mapped_column(ForeignKey("bookings.id"), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    provider: Mapped[str] = mapped_column(Enum(Provider), default=Provider.PAYSTACK)
    reference: Mapped[str] = mapped_column(String(60), nullable=False, default=lambda: str(uuid4()))
    payment_status: Mapped[str] = mapped_column(Enum(PaymentStatus), default=PaymentStatus.PENDING)
    payment_method: Mapped[str] = mapped_column(Enum(PaymentMethod), default=PaymentMethod.CARD)



    booking: Mapped["Booking"] = relationship(back_populates="payments")
    user: Mapped["User"] = relationship(back_populates="payments")
    
