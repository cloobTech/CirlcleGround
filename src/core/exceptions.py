from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class CircleGround(Exception):
    """Base class for all CircleGround exceptions."""
    message: str
    details: Optional[Any] = None


class UniqueViolationError(CircleGround):
    def __init__(self, message="Unique violation", details=None):
        super().__init__(message=message, details=details)


class EntityNotFound(CircleGround):
    def __init__(self, message="Entity not found", details=None):
        super().__init__(message=message, details=details)

class EntityAlreadyExist(CircleGround):
    def __init__(self, message="Entity already exist", details=None):
        super().__init__(message=message, details=details)

class UserAlreadyExistsError(CircleGround):
    def __init__(self, message="User already exist", details=None):
        super().__init__(message=message, details=details)


class UserNotFound(CircleGround):
    def __init__(self, message="Service provider not found", details=None):
        super().__init__(message=message, details=details)


class PermissionDeniedError(CircleGround):
    def __init__(self, message="Permission denied", details=None):
        super().__init__(message=message, details=details)


class AmenityNotFoundError(CircleGround):
    def __init__(self, message="Amenity not found", details=None):
        super().__init__(message=message, details=details)


class SpaceAmenityNotFoundError(CircleGround):
    def __init__(self, message="Space amenity not found", details=None):
        super().__init__(message=message, details=details)


class StoreAlreadyExistsError(CircleGround):
    def __init__(self, message="Store already exist", details=None):
        super().__init__(message=message, details=details)


class ConflictError(CircleGround):
    def __init__(self, message="Conflict", details=None):
        super().__init__(message=message, details=details)


class LocationAlreadyExistsError(CircleGround):
    def __init__(self, message="Location already exist", details=None):
        super().__init__(message=message, details=details)


class InvalidCredentialsError(CircleGround):
    def __init__(self, message="Invalid Credentials", details=None):
        super().__init__(message=message, details=details)


class DatabaseConnectionError(CircleGround):
    def __init__(self, message="Failed to connect to database", details=None):
        super().__init__(message=message, details=details)


class PasswordMismatchError(CircleGround):
    def __init__(self, message="Password mismatch", details=None):
        super().__init__(message=message, details=details)


class InvalidResetTokenError(CircleGround):
    def __init__(self, message="Invalid or expired reset token", details=None):
        super().__init__(message=message, details=details)


class EmailServiceError(CircleGround):
    def __init__(self, message="Error sending email", details=None):
        super().__init__(message=message, details=details)
