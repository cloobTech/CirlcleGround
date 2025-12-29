from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class CircleGround(Exception):
    """Base class for all CircleGround exceptions."""
    message: str
    details: Optional[Any] = None

class UserAlreadyExist(CircleGround):
    def __init__(self, message="user already exist", details=None):
        super().__init__(message=message, details=details)

class UserNotFound(CircleGround):
    def __init__(self, message="service provider not found", details=None):
        super().__init__(message=message, details=details)

class DatabaseConnectionError(CircleGround):
    def __init__(self, message="failed to connect to database", details=None):
        super().__init__(message=message, details=details)