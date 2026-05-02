from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, Enum
from decimal import Decimal
from src.models.basemodel import Basemodel, Base
from src.enums.enums import Currency



if TYPE_CHECKING:
    from src.models.user import User
    from src.models.wallet_transaction import WalletTransaction




class Wallet(Basemodel, Base):
    __tablename__="wallets"

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
    account_number: Mapped[str] = mapped_column(nullable=False)
    balance: Mapped[Decimal] = mapped_column(nullable=False)
    currency: Mapped[str] = mapped_column(Enum(Currency), nullable=False)
    wallet_pin: Mapped[str]  = mapped_column(nullable=False)


    user: Mapped["User"] = relationship(back_populates="wallet")

    wallet_transactions: Mapped[list["WalletTransaction"]] = relationship(back_populates="wallet")
