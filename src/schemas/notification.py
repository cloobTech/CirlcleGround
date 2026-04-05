from pydantic import BaseModel
from src.enums.enums import NotificationType


class CreateNotification(BaseModel):
    """Event emitted when a new notification is created"""
    title: str
    message: str
    sender_id: str | None = None
    notification_type: NotificationType
    resource_id: str | None = None
