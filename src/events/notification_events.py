from src.events.base import DomainEvent
from src.schemas.notification import CreateNotification


class NotificationCreatedEvent(DomainEvent):
    """Event emitted when a new notification is created"""
    data: CreateNotification
    recipient_ids: list[str]
