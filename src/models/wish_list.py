from typing import TYPE_CHECKING
from src.models.basemodel import Basemodel, Base
from sqlalchemy import ForeignKey,  UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from src.models.user import User
    from src.models.space import Space


class WishList(Basemodel, Base):
    __tablename__ = "wishlists"
    __table_args__ = (
        UniqueConstraint("user_id", "space_id",
                         name="unique_user_space_wishlist"),
    )

    user_id: Mapped[str] = mapped_column(ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    space_id: Mapped[str] = mapped_column(ForeignKey(
        "spaces.id", ondelete="CASCADE"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="wishlist_items")
    space: Mapped["Space"] = relationship(back_populates="wishlisted_by")
