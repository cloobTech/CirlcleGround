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

class Status(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    REVERSED = "cancelled"
    NOT_PAID = "not_paid"