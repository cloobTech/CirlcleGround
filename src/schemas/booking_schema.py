from pydantic import BaseModel


class BaseBooking(BaseModel):
    pass


class CreateBookingSchema(BaseModel):
    space_id: str
    start_time: str
    end_time: str
    total_price: float
