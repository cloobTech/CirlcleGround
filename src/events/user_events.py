from src.events.base import DomainEvent

class BaseUserEvent(DomainEvent):
    email: str
    first_name: str
    last_name: str
    token: str

class UserCreatedEvent(BaseUserEvent):
    pass

class RequestPasswordResetEvent(BaseUserEvent):
    pass