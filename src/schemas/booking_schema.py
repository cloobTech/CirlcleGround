from pydantic import BaseModel
from src.enums.enums import BookingStatus
from datetime import datetime


class BaseBooking(BaseModel):
    pass


class BookingAddonSchema(BaseModel):
    addon_id: str


class CreateBookingSchema(BaseModel):
    space_id: str
    start_time: datetime
    end_time: datetime
    
    addon_ids: list[str]


class BookingHistorySchema(BaseModel):
    note: str
    status: BookingStatus = BookingStatus.PENDING


class   UpdateBookingSchema(BaseModel):
    start_time: datetime | None = None
    end_time: datetime | None = None


class UpdateBookingSchemaByHost(BaseModel):
    status: BookingStatus
    start_time: datetime | None = None
    end_time: datetime | None = None


class BookingQueryParams(BaseModel):
    status: BookingStatus | None = None
