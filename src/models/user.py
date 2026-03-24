from datetime import datetime
from sqlalchemy import Enum, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.basemodel import Base, Basemodel, SoftDeleteMixin
from src.enums.enums import UserRole
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.booking import Booking
    from src.models.reviews import Review
    from src.models.space import Space
    from src.models.wish_list import WishList
    from src.models.notification import Notification
    from src.models.notification_recipient import NotificationRecipient


class User(Basemodel, Base, SoftDeleteMixin):
    __tablename__ = "users"

    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    phone_number: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    latitude: Mapped[float | None] = mapped_column(nullable=True)
    longitude: Mapped[float | None] = mapped_column(nullable=True)
    location: Mapped[str | None] = mapped_column(nullable=True)
    profile_image: Mapped[str | None] = mapped_column(nullable=True)

    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole),
        default=UserRole.GUEST_USER
    )

    is_email_verified: Mapped[bool] = mapped_column(default=False)

    verification_token: Mapped[str | None] = mapped_column(
        nullable=True,
        default=None
    )

    verification_token_expires_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    last_login: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    is_super_admin: Mapped[bool] = mapped_column(default=False, nullable=False)

    bookings: Mapped[list["Booking"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

    reviews_written: Mapped[list["Review"]] = relationship(
        back_populates="reviewer",
        foreign_keys="[Review.reviewer_id]",
        cascade="all, delete-orphan"
    )
    reviews_received: Mapped[list["Review"]] = relationship(
        back_populates="reviewee",
        foreign_keys="[Review.reviewee_id]",
        cascade="all, delete-orphan"
    )

    spaces: Mapped[list["Space"]] = relationship(
        back_populates="host",
        cascade="all, delete-orphan"
    )

    wishlist_items: Mapped[list["WishList"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

    sent_notifications: Mapped[list["Notification"]] = relationship(
        back_populates="sender",
        cascade="all, delete-orphan"
    )

    notification_recipients: Mapped[list["NotificationRecipient"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )
