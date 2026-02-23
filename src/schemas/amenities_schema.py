from pydantic import BaseModel
from src.enums.enums import AmenityCategory


class BaseAmenity(BaseModel):
    name: str
    category: AmenityCategory = AmenityCategory.CUSTOM


class CreateAmenity(BaseModel):
    amenities: list[BaseAmenity]


class DeleteAmenity(BaseModel):
    amenity_id: str

class DeleteMultipleAmenities(BaseModel):
    amenities_id : list[DeleteAmenity]

    def get_ids(self) -> list[str]:
        """Extract list of amenity IDs as strings"""
        return [item.amenity_id for item in self.amenities_id]
