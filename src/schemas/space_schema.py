from pydantic import BaseModel, Field, ConfigDict
from src.enums.enums import SpaceType, SpaceCategory, SpaceStatus, SpacePriceType, BookingStatus
from datetime import datetime, time
from decimal import Decimal


class SpaceSchema(BaseModel):
    price_per_hour: Decimal
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


class SpaceQueryParams(BaseModel):
    booking_status: BookingStatus | None = None
    include_bookings: bool = False
    space_status: SpaceStatus | None = None


class CreateSpaceBlackout(BaseModel):
    
    start_datetime: datetime
    end_datetime: datetime
    reason: str

class ReadSpaceBlackout(BaseModel):
    id: str
    start_datetime: datetime
    end_datetime: datetime
    reason: str

model_config = ConfigDict(from_attributes=True)
