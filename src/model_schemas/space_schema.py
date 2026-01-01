from pydantic import BaseModel


class CreateSpaceSchema(BaseModel):
    location_id: str
    description: str
    max_guests: str
