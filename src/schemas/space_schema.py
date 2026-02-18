from pydantic import BaseModel, Field
from src.enums.enums import SpaceType, SpaceCategory, SpaceStatus, SpacePriceType
from datetime import datetime, time


class SpaceSchema(BaseModel):
    location_id: str
    name: str
    description: str
    price: float
    max_guests: int
    space_type: SpaceType = SpaceType.OTHERS
    category: SpaceCategory = SpaceCategory.OTHERS
    is_verified: bool = False
    square_feet: int
    length: int
    width: int
    num_of_bathrooms: int = 0
    num_of_toilets: int = 0
    num_of_parking_spaces: int = 0


class SpaceImageSchema(BaseModel):
    url: str
    order: int


class SpaceUseCaseSchema(BaseModel):
    name: str
    description: str


class SpaceRuleSchema(BaseModel):
    title: str
    description: str


class SpacePricingSchema(BaseModel):
    price_type: SpacePriceType
    price: float
    currency: str = "NGN"
    start_date: datetime
    end_date: datetime


class SpaceAddonSchema(BaseModel):
    name: str
    description: str
    price: float
    currency: str = "NGN"


class SpaceCustomAmenitySchema(BaseModel):
    name: str


class SpaceOperationHourSchema(BaseModel):
    day_of_week: int = Field(..., ge=0, le=6)
    open_time: time | None = None
    close_time: time | None = None
    is_closed: bool = False


class CreateSpaceSchema(BaseModel):
    space: SpaceSchema


class UpdateSpaceAtCreation(BaseModel):
    use_cases: list[SpaceUseCaseSchema] = []
    rules: list[SpaceRuleSchema] = []
    pricings: list[SpacePricingSchema]
    addons: list[SpaceAddonSchema] = []
    custom_amenities: list[SpaceCustomAmenitySchema] = []
    amenity_ids: list[str] = []
    status: SpaceStatus
    operation_hours: list[SpaceOperationHourSchema]
