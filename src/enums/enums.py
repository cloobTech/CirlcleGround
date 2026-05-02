from enum import Enum


class ActiveStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class DaysOfTheWeek(str, Enum):
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
    UNPAID = "unpaid"

class PaymentMethod(str, Enum):
    CARD = "card"
    TRANSFER = "transfer"

class Provider(str, Enum):
    PAYSTACK = "paystack"

class BookingStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    EXPIRED = "expired"
    ACTIVE = "active"
    INACTIVE = "inactive"
    CHECKED_IN = "checked_in"
    CHECKED_OUT = "checked_out"

class WalletTransactionPurpose(str, Enum):
    TOP_UP = "top_up"
    WITHDRAWAL = "withdrawal"
    REFUND = "refund"
    BOOKING_PAYMENT = "booking_payment"
    TRANSFER = "transfer"

class WalletTransactionStatus(str, Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"

class TransactionType(str, Enum):
    DEBIT = "debit"
    CREDIT = "credit"

class Currency(str, Enum):
    NGN = "ngn"
    USD = "usd"

class PaymentAction(str, Enum):
    STOP = "stop"
    REUSE = "reuse"
    CREATE_NEW = "create_new"
    CREATE_BALANCE = "create_balance" 


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
    TEMP = "temp"
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


class BookingPaymentStatus(str, Enum):
    UNPAID = "unpaid"
    PAID = "paid"
    REFUNDED = "refunded"
    PARTIALLY_PAID = "partially_paid"
    DECLINED = "declined"
    


class AmenityCategory(str, Enum):
    BASIC = "basic"
    WORKSPACE = "workspace"
    TECHNOLOGY = "technology"
    COMFORT = "comfort"
    SAFETY = "safety"
    OUTDOOR = "outdoor"
    PARKING = "parking"
    CUSTOM = "custom"


class NotificationType(str, Enum):
    BOOKING_REQUESTED = "booking_requested"
    BOOKING_ACCEPTED = "booking_accepted"
    BOOKING_DECLINED = "booking_declined"
    BOOKING_CANCELLED = "booking_cancelled"
    BOOKING_CONFIRMED = "booking_confirmed"
    CHECK_IN_REMINDER = "check_in_reminder"
    CHECK_OUT_REMINDER = "check_out_reminder"
    SPACE_CREATION = "space_creation"
    PAYMENT_SUCCESS = "payment_success"
    PAYMENT_FAILED = "payment_failed"
    EMAIL_VERIFIED = "email_verified"

class ReviewType(str, Enum):
    HOST_TO_GUEST_USER = "host_to_guest_user"
    GUEST_USER_TO_SPACE = "guest_user_to_space"

class ResourceType(str, Enum):
    BOOKING = "booking"
    SPACE = "space"
    PAYMENT = "payment"
    MESSAGE = "message"
    USER = "user"
    REVIEW = "review"
    WISHLIST = "wishlist"


class ActivityType(str, Enum):

    USER_CREATED = "user_created"
    USER_LOGIN = "user_login"
    USER_UPDATED = "user_updated"
    USER_DELETED = "user_deleted"
    PASSWORD_CHANGED = "password_changed"
    EMAIL_VERIFIED = "email_verified"
    ADMIN_CREATED = "admin_created"
    SPACE_CREATED = "space_created"
    SPACE_UPDATED = "space_updated"
    SPACE_DELETED = "space_deleted"
    BOOKING_CREATED = "booking_created"
    BOOKING_DELETED = "booking deleted"
    BOOKING_UPDATED = "booking_updated"
    BOOKING_CANCELLED = "booking_cancelled"
    BOOKING_APPROVED = "booking_approved"
    BOOKING_REJECTED = "booking_rejected"
    PAYMENT_INITIATED = "payment_initiated"
    PAYMENT_COMPLETED = "payment_completed"
    PAYMENT_FAILED = "payment_failed"
    PAYMENT_REFUNDED = "payment_refunded"
    MESSAGE_SENT = "message_sent"
    MESSAGE_DELETED = "message_deleted"
    MESSAGE_UPDATED = "message_updated"
    REVIEW_SENT = "review_sent"
    REVIEW_UPDATED = "review_updated"
    REVIEW_DELETED = "review_deleted"
    SPACE_REVIEWS_DELETED = "space_reviews_deleted"
    WISHLIST_ADDED = "favorite_added"
    WISHLIST_REMOVED = "favorite_removed"