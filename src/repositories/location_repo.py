from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.repositories.base import BaseRepository
from src.models.location import Location


class LocationRepository(BaseRepository[Location]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Location, session)
    
    async def check_by_region(self, country: str, state: str, city: str):
        result = await self.session.execute(select(Location).where(
            Location.country == country,
            Location.state == state,
            Location.city == city
            ))
        return result.scalar_one_or_none()
    