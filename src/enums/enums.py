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
    COMPLETED = "completed"
    EXPIRED = "expired"


class UserRole(str, Enum):
    ADMIN = "admin"
    GUEST_USER = "guest_user"
    HOST = "host"
    SUPER_ADMIN = "super_admin"


class SpaceType(str, Enum):
    APARTMENT = "apartment"
    HOUSE = "house"
    STUDIO = "studio"
    OFFICE = "office"
    HALL = "hall"
    WAREHOUSE = "warehouse"
    SHOP = "shop"
    OUTDOOR = "outdoor"
    HOTEL_ROOM = "hotel_room"
    OTHERS = "others"


class SpaceCategory(str, Enum):
    SHORT_STAY = "short stay"
    MEETING = "meeting"
    EVENT = "event"
    PHOTOSHOOT = "photoshoot"
    WORKSHOP = "workshop"
    PARTY = "party"
    STORAGE = "storage"
    COWORKING = "coworking"
    OTHERS = "others"


class SpacePriceType(str, Enum):
    HOURLY = "hourly"
    WEEKLY = "weekly"
    DAILY = "daily"
    MONTHLY = "monthly"
    YEARLY = "yearly"


class SpaceStatus(str, Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    INACTIVE = "inactive"
    PUBLISHED = "published"
    PENDING = "pending"
    REJECTED = "rejected"


class ImageStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    PROCESSING = "processing"
    FAILED = "failed"