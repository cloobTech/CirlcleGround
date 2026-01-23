from pydantic import BaseModel


class BaseAmenity(BaseModel):
    name: str
