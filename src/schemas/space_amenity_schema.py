from pydantic import BaseModel

class BaseSpaceAmenity(BaseModel):
    space_amenity_id: str

class MultipleSpaceAmenities(BaseModel):
    space_amenities_id: list[BaseSpaceAmenity]
