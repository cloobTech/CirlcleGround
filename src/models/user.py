from models.base import Basemodel, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
# 

class User(Basemodel, Base):
    __tablename__ ="users"

    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_email_verfied: Mapped[bool] = mapped_column(default=False)
    reset_token: Mapped[str] = mapped_column(default=False, nullable=True)
    preferred_location: Mapped[str] = mapped_column(nullable=False)
    is_deleted: Mapped[bool] = mapped_column(default=False)
    role: Mapped[str] = mapped_column(nullable=False)

    
    #relationships(One-one)
    # customer: Mapped["Customer"] = relationship(back_populates="user", uselist=False, cascade="all, delete-orphan")

    host: Mapped["Host"] = relationship(back_populates="user", uselist=False, cascade="all, delete-orphan")

    #(one-many)
    bookings: Mapped[list["Booking"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    reviews: Mapped[list["Review"]] = relationship(back_populates="user", cascade="all, delete-orphan")