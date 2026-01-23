from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.base import BaseRepository
from src.models.location import Location


class LocationRepository(BaseRepository[Location]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Location, session)

    