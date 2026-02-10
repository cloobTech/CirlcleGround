from pydantic import BaseModel


class CreateSpaceSchema(BaseModel):
    location_id: str
    name: str
    description: str
    price: str
    max_guests: str
