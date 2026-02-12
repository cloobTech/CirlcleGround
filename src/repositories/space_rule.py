from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.space_rule import SpaceRule


class SpaceRuleRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(SpaceRule, session)
        