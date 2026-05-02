from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from src.models.basemodel import Basemodel, Base

if TYPE_CHECKING:
    from src.models.user import User



class BankAccount(Basemodel, Base):
    __tablename__="bank_accounts"

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    account_number: Mapped[str] = mapped_column(nullable=False)
    account_name: Mapped[str] = mapped_column(nullable=False)
    # bank_name: Mapped[str] = mapped_column(nullable=False)
    bank_code: Mapped[str] = mapped_column(nullable=False)
    recipient: Mapped[str] = mapped_column(nullable=False)
    currency: Mapped[str] = mapped_column(nullable=False)


    user: Mapped["User"] = relationship(back_populates="bank_account")