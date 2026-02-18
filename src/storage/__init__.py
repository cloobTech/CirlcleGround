from src.core.pydantic_confirguration import config
from src.storage.database import Database
from src.storage.sync_db import SyncDBStorage
from src.models.user import User
from src.models import (user, reviews, booking, payments, location, amenities, space, space_amenities, space_addon,
                        space_image, space_pricing, space_rule, custom_amenity, space_use_case, space_blackout, space_operating_hour,
                        booking_history, booking_addon)


__all__ = [
    "User"
]


SYNC_DATABASE_URL = config.DATABASE_URL.replace(
    "postgresql+asyncpg", "postgresql+psycopg2")
db = Database()
sync_db = SyncDBStorage()
