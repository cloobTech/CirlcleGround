from typing import Type
from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, delete
from sqlalchemy.orm import selectinload
from src.repositories.base import BaseRepository
from src.models.reviews import Review
from src.schemas.reviews_schema import SendReviewSchema


class ReviewRepository(BaseRepository[Review]):
    def __init__(self, session: AsyncSession):
        super().__init__(Review, session)

 
    
    async def get_booking_review(self, booking_id: str, reviewer_id: str):
        stmt = (
            select(self.model)
            .where(
            self.model.booking_id == booking_id,
            self.model.reviewer_id == reviewer_id
        )
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    
    async def get_review(self, review_id: str):
        stmt = select(self.model).where(self.model.id == review_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    

    async def get_space_reviews(self, space_id: str):
        stmt = (
            select(self.model)
            .where(self.model.space_id == space_id)
            .options(
                selectinload(self.model.reviewer),
                selectinload(self.model.reviewee)
            )
            .order_by(self.model.created_at.desc())
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()
    

    async def get_space_rating(self, space_id: str):
        stmt = select(func.avg(self.model.rating)).where(self.model.space_id == space_id)
        result = await self.session.execute(stmt)
        return result.scalar() or 0
    
    async def delete_space_reviews(self, space_id: str, soft: bool = False):
        stmt = select(self.model).where(self.model.space_id == space_id)
        result = await self.session.execute(stmt)
        reviews = result.scalars().all()


        for review in reviews:
            if soft and self.supports_soft_delete:
                review.is_deleted = True
                review.deleted_at = datetime.now(timezone.utc)
            else:
                await self.session.delete(review)
        return True