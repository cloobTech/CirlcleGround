from models.base import Basemodel, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import Optional

class User(Basemodel, Base):
    __tablename__ ="users"

    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_email_verfied: Mapped[bool] = mapped_column(default=False)
    reset_token: Mapped[str] = mapped_column(default=False, nullable=True)
    role: Mapped[str] = mapped_column(nullable=False)

    
    #relationships(One-one)
    customer: Mapped["Customer"] = relationship(back_populates="user", uselist=False)
    host: Mapped["Host"] = relationship(back_populates="user", uselist=False)

    #(one-many)
    booking: Mapped[list["Booking"]] = relationship(back_populates="user", uselist=True)

    review: Mapped[list["Review"]] = relationship(back_populates="user", uselist=True)