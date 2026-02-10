from pydantic import BaseModel


class LocationSchema(BaseModel):
    country: str
    city: str
    state: str