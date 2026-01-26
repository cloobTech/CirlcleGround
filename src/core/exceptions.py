from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class CircleGround(Exception):
    """Base class for all CircleGround exceptions."""
    message: str
    details: Optional[Any] = None

class UserAlreadyExistsError(CircleGround):
    def __init__(self, message="user already exist", details=None):
        super().__init__(message=message, details=details)

class UserNotFound(CircleGround):
    def __init__(self, message="service provider not found", details=None):
        super().__init__(message=message, details=details)
        
class PermissionDeniedError(CircleGround):
    def __init__(self, message="Permission denied", details=None):
        super().__init__(message=message, details=details)

class StoreAlreadyExistsError(CircleGround):
    def __init__(self, message="store already exist", details=None):
        super().__init__(message=message, details=details)

class LocationAlreadyExistsError(CircleGround):
    def __init__(self, message="location already exist", details=None):
        super().__init__(message=message, details=details)   
     
class InvalidCredentialsError(CircleGround):
    def __init__(self, message="Invalid Credentials", details=None):
        super().__init__(message=message, details=details)

class DatabaseConnectionError(CircleGround):
    def __init__(self, message="failed to connect to database", details=None):
        super().__init__(message=message, details=details)