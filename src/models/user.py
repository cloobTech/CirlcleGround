from src.models.basemodel import Basemodel, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.booking import Booking
    from src.models.reviews import Review


class User(Basemodel, Base):
    __tablename__ ="users"

    name: Mapped[str] = mapped_column(nullable=False)
    # last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    location: Mapped[str] = mapped_column(nullable=False)
    phone_number: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    confirm_password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(nullable=False, default="user")
    is_user_verified: Mapped[bool] = mapped_column(nullable=False, default=False)
    is_email_verfied: Mapped[bool] = mapped_column(default=False)
    reset_token: Mapped[str] = mapped_column(default=False, nullable=True)
    location: Mapped[str] = mapped_column(nullable=False)
    last_login: Mapped[str] = mapped_column(default=False)
    is_deleted: Mapped[bool] = mapped_column(default=False)



    
    


    


    #(one-many)
    bookings: Mapped[list["Booking"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    reviews: Mapped[list["Review"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    
    