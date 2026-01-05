from enum import Enum

class ActiveStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class DaysOfTheWeek(Enum):
    SUNDAY = "sunday"
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"

class PaymentStatus(str, Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"

class BookingStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    EXPIRED = "expired"

class UserRole(str, Enum):
    ADMIN = "admin"
    CUSTOMER = "customer"
    HOST = "host"
    