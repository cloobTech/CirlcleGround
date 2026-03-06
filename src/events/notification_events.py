from src.events.base import DomainEvent
from src.enums.enums import NotificationType


class NotificationCreatedEvent(DomainEvent):
    """Event emitted when a new notification is created"""

    notification_id: str
