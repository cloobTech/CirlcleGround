from sqlalchemy import select, exists, func
from sqlalchemy.orm import selectinload, with_loader_criteria
from src.models.space import Space
from src.models.booking import Booking
from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.space_schema import SpaceSchema, SpaceQueryParams


class SpaceRepository(BaseRepository[Space]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Space, session)

    async def create_space(self, host_id: str, data: SpaceSchema) -> Space:
        space = Space(host_id=host_id, **data.model_dump())
        created_space = await self.create(space)
        return created_space
    

    async def get_user_spaces(self, user_id: str, params: SpaceQueryParams):
        stmt = select(Space).where(Space.host_id == user_id)

        if params.booking_status:
            stmt = stmt.where(
                exists().where(
                    (Booking.space_id == Space.id) &
                    (Booking.status == params.booking_status)
                )
            )

        if params.include_bookings:
            stmt = stmt.options(
                selectinload(Space.bookings),
                with_loader_criteria(
                    Booking,
                    Booking.status == params.booking_status,
                    include_aliases=True,
                )
            )

        if params.space_status:
            stmt = stmt.where(Space.status == params.space_status)

        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_space_by_id(self, space_id: str):
        space = await self.get_by_id(space_id)
        return space

    async def search_spaces(self, query: str, limit: int = 10):
        stmt = select(Space)

        # Only apply TSVector search if we are on Postgres
        if self.session.bind.dialect.name == "postgresql":
            stmt = stmt.where(
                Space.search_vector.match(query)
            ).order_by(
                func.ts_rank_cd(Space.search_vector,
                                func.websearch_to_tsquery(query)).desc()
            )
        else:
            # Fallback for SQLite: simple ILIKE on name/description
            stmt = stmt.where(
                (Space.name.ilike(f"%{query}%")) |
                (Space.description.ilike(f"%{query}%")) | 
                (Space.space_type.ilike(f"%{query}%")) |
                (Space.category.ilike(f"%{query}%"))
            )

        stmt = stmt.limit(limit)
        result = await self.session.execute(stmt)
        return result.scalars().all()
