from pydantic import BaseModel
from src.enums.enums import AmenityCategory


class BaseAmenity(BaseModel):
    name: str
    category: AmenityCategory = AmenityCategory.CUSTOM


class CreateAmenity(BaseModel):
    amenities: list[BaseAmenity]


class DeleteAmenity(BaseModel):
    amenity_id: str

class DeleteMultipleSpaceAmenities(BaseModel):
    space_amenities_id : list[DeleteAmenity]
