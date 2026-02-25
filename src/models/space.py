from typing import TYPE_CHECKING
from src.models.basemodel import Basemodel, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text, Enum
from src.enums.enums import SpaceType, SpaceCategory, SpaceStatus

# from models.association import space_amenity_link


if TYPE_CHECKING:
    from src.models.location import Location
    from src.models.reviews import Review
    from src.models.space_amenities import SpaceAmenity
    from src.models.user import User
    from src.models.space_image import SpaceImage
    from src.models.space_rule import SpaceRule
    from src.models.space_pricing import SpacePricing
    from src.models.space_addon import SpaceAddon
    from src.models.custom_amenity import CustomAmenity
    from src.models.booking import Booking
    from src.models.space_use_case import SpaceUseCase
    from src.models.space_blackout import SpaceBlackout
    from src.models.space_operating_hour import SpaceOperatingHour
    from src.models.wish_list import WishList


class Space(Basemodel, Base):
    __tablename__ = "spaces"

    location_id: Mapped[str] = mapped_column(
        ForeignKey("locations.id"), nullable=False)
    host_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"), nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    max_guests: Mapped[int] = mapped_column(nullable=False)
    space_type: Mapped[SpaceType] = mapped_column(
        Enum(SpaceType), nullable=False, default=SpaceType.OTHERS)
    category: Mapped[SpaceCategory] = mapped_column(
        Enum(SpaceCategory), nullable=False, default=SpaceCategory.OTHERS)
    status: Mapped[SpaceStatus] = mapped_column(
        Enum(SpaceStatus), nullable=False, default=SpaceStatus.TEMP)
    is_verified: Mapped[bool] = mapped_column(default=False)
    square_feet: Mapped[int] = mapped_column(nullable=False)
    length: Mapped[int] = mapped_column(nullable=False)
    width: Mapped[int] = mapped_column(nullable=False)
    num_of_bathrooms: Mapped[int] = mapped_column(nullable=False, default=0)
    num_of_toilets: Mapped[int] = mapped_column(nullable=False, default=0)
    num_of_parking_spaces: Mapped[int] = mapped_column(
        nullable=False, default=0)

    host: Mapped["User"] = relationship(back_populates="spaces")

    location: Mapped["Location"] = relationship(back_populates="spaces")

    images: Mapped[list["SpaceImage"]] = relationship(
        back_populates="space", cascade="all, delete-orphan")

    rules: Mapped[list["SpaceRule"]] = relationship(
        back_populates="space", cascade="all, delete-orphan")

    pricings: Mapped[list["SpacePricing"]] = relationship(
        back_populates="space", cascade="all, delete-orphan")

    space_addons: Mapped[list["SpaceAddon"]] = relationship(
        back_populates="space", cascade="all, delete-orphan")

    custom_amenities: Mapped[list["CustomAmenity"]] = relationship(
        back_populates="space", cascade="all, delete-orphan")

    bookings: Mapped[list["Booking"]] = relationship(
        back_populates="space", cascade="all, delete-orphan")

    use_cases: Mapped[list["SpaceUseCase"]] = relationship(
        back_populates="space", cascade="all, delete-orphan")

    operating_hours: Mapped[list["SpaceOperatingHour"]] = relationship(
        back_populates="space", cascade="all, delete-orphan")

    blackouts: Mapped[list["SpaceBlackout"]] = relationship(
        back_populates="space", cascade="all, delete-orphan")

    wishlisted_by: Mapped[list["WishList"]] = relationship(
        back_populates="space", cascade="all, delete-orphan")

    # NOT CHECKED YET

    reviews: Mapped[list["Review"]] = relationship(
        back_populates="space", cascade="all, delete-orphan")

    space_amenities: Mapped[list["SpaceAmenity"]] = relationship(
        back_populates="spaces",
        cascade="all, delete-orphan"
    )
