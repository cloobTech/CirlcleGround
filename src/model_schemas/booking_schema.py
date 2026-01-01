from pydantic import BaseModel


class CreateBookingSchema(BaseModel):
    guest_id: str
    space_id: str
    status: str
    start_time: str
    end_time: str
    cancelled_time: str
