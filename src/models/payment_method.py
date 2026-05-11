from sqlalchemy.orm import mapped_column, relationship, Mapped
from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import DateTime, Enum, ForeignKey
from src.models.basemodel import Basemodel, Base
from src.enums.enums import CardType



if TYPE_CHECKING:
    from src.models.user import User


class PaymentMethod(Basemodel, Base):
    __tablename__="payment_methods"

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
    last_four_digits: Mapped[str] = mapped_column(nullable=False)
    authorization_code: Mapped[str] = mapped_column(nullable=False)
    expiry_date: Mapped[str] = mapped_column(nullable=False)
    is_default: Mapped[bool] = mapped_column(default=False)
    reusable: Mapped[bool] = mapped_column(default=True)
    card_type: Mapped[str] = mapped_column(nullable=False)




    user: Mapped["User"] = relationship(back_populates="payment_methods")