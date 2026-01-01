from pydantic import BaseModel


class CreateAmenitySchema(BaseModel):
    name: str