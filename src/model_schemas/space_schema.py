from pydantic import BaseModel


class CreateSpaceSchema(BaseModel):
    location_id: str
    name: str
    description: str
    max_guests: str
