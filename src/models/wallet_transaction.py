from src.models.basemodel import Basemodel, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum
from typing import TYPE_CHECKING
from decimal import Decimal
from sqlalchemy import ForeignKey
from src.enums.enums import PaymentStatus, TransactionType,  WalletTransactionPurpose


if TYPE_CHECKING:
    from src.models.wallet import Wallet



class WalletTransaction(Basemodel, Base):
    __tablename__="wallet_transactions"

    wallet_id: Mapped[str] = mapped_column(ForeignKey("wallets.id"), nullable=False)
    amount: Mapped[Decimal] = mapped_column(nullable=False)
    type: Mapped[TransactionType] = mapped_column(Enum(TransactionType), nullable=False)
    purpose: Mapped[WalletTransactionPurpose] = mapped_column(Enum(WalletTransactionPurpose), nullable=False)
    status: Mapped[PaymentStatus] = mapped_column(Enum(PaymentStatus), default=PaymentStatus.PENDING, nullable=False)
    reference: Mapped[str] = mapped_column(nullable=False)




    wallet: Mapped["Wallet"] = relationship(back_populates="wallet_transactions")


