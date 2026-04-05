from sqlalchemy import select
from src.repositories.base import BaseRepository
from src.models.activity_log import ActivityLog
from src.schemas.activity_log_schema import ActivityLogSchema



class ActivityLogRepository(BaseRepository[ActivityLog]):
    def __init__(self, session):
        super().__init__(ActivityLog, session)
    
    async def log_activity(self, activity_log_data: ActivityLogSchema)->ActivityLog:
        data = activity_log_data.model_dump()
        activity = ActivityLog(**data)
        logged_activity = await self.create(activity)
        return logged_activity

    async def get_user_activities(self, user_id: str):
        stmt = select(self.model).where(self.model.user_id == user_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()
