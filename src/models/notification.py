from typing import TYPE_CHECKING
from sqlalchemy import String,  Text, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.basemodel import Basemodel, Base
from src.enums.enums import NotificationType

if TYPE_CHECKING:
    from src.models.user import User
    from src.models.notification_recipient import NotificationRecipient


class Notification(Basemodel, Base):
    """Notification Class"""
    __tablename__ = "notifications"

    sender_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"), nullable=True
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    notification_type: Mapped[NotificationType] = mapped_column(
        Enum(NotificationType), nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    resource_id: Mapped[str] = mapped_column(nullable=True)

    sender: Mapped["User"] = relationship(
        back_populates="sent_notifications"
    )

    recipients: Mapped[list["NotificationRecipient"]] = relationship(
        back_populates="notification",
        cascade="all, delete-orphan"
    )
