from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.space_rule import SpaceRule
from src.schemas.space_schema import SpaceRuleSchema


class SpaceRuleRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(SpaceRule, session)

    async def create(self, space_id: str, data: SpaceRuleSchema) -> SpaceRule:
        space_rule = SpaceRule(space_id=space_id, **data.model_dump())
        return await super().create(space_rule)
