from src.models.activity_log import ActivityLog
from src.unit_of_work.unit_of_work import UnitOfWork
from src.schemas.activity_log_schema import ActivityLogSchema


class ActivityLogService:
    def __init__(self, uow_factory: UnitOfWork):
        self.uow_factory = uow_factory

    async def get_user_activity_logs(self, user_id: str):
        async with self.uow_factory as uow:
            activity_logs = await uow.activity_repo.get_user_activities(user_id)
            return activity_logs
        
    async def get_activity_log(self, activity_log_id: str):
        async with self.uow_factory as uow:
            activity_log = await uow.activity_repo.get_by_id(activity_log_id)
            return activity_log