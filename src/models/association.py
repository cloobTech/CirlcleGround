from sqlalchemy import ForeignKey, Table, Column
from models.base import Base
from sqlalchemy.orm import mapped_column, Mapped


# Association tables for many-to-many
space_amenity_link = Table(
    "space_amenity_link",
    Base.metadata,
    Column("space_id", ForeignKey("spaces.id"), primary_key=True),
    Column("amenity_id", ForeignKey("amenities.id"), primary_key=True)
)