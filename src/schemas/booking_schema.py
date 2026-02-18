from pydantic import BaseModel
from src.enums.enums import BookingStatus


class BaseBooking(BaseModel):
    pass


class BookingAddonSchema(BaseModel):
    addon_id: str


class CreateBookingSchema(BaseModel):
    space_id: str
    start_time: str
    end_time: str
    total_price: float
    addon_ids: list[str]


class BookingHistorySchema(BaseModel):
    note: str
    status: BookingStatus = BookingStatus.PENDING
