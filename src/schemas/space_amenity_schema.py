from pydantic import BaseModel

class BaseSpaceAmenity(BaseModel):
    space_amenity_id: str

class MultipleSpaceAmenities(BaseModel):
    space_amenities_id: list[BaseSpaceAmenity]

    def get_ids(self) -> list[str]:
        """Extract list of amenity IDs as strings"""
        return [item.space_amenity_id for item in self.space_amenities_id]