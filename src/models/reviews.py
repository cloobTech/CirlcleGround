from src.models.basemodel import Basemodel, Base, SoftDeleteMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.enums.enums import ReviewType
from typing import Optional

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.models.user import User
    from src.models.space import Space
    from src.models.booking import Booking



class Review(Basemodel, Base, SoftDeleteMixin):
    __tablename__ ="reviews"

    reviewer_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
    reviewee_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
    booking_id: Mapped[str] = mapped_column(ForeignKey("bookings.id"), nullable=False)
    space_id: Mapped[str] = mapped_column(ForeignKey("spaces.id"), nullable=False)
    review_type: Mapped[str] = mapped_column(default=ReviewType.GUEST_USER_TO_SPACE)
    comment: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[int] = mapped_column(nullable=False)
    


    reviewer: Mapped["User"] = relationship(back_populates="reviews_written", foreign_keys=[reviewer_id])
    reviewee: Mapped["User"] = relationship(back_populates="reviews_received", foreign_keys=[reviewee_id])

    space: Mapped["Space"] = relationship(back_populates="reviews")
    booking: Mapped["Booking"] = relationship(back_populates="reviews")