from src.events.base import DomainEvent
from src.schemas.messaging import MessageSchema


class MessageCreatedEvent(DomainEvent):
    message: MessageSchema
    recipient_ids: list[str]
