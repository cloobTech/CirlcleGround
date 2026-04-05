from fastapi import APIRouter, Depends
from src.api.v1.dependencies import get_current_user, get_activity_log_service
from src.services.activity_log_services import ActivityLogService
from src.models.user import User


activity_log_router = APIRouter(prefix="/api/v1/activity_logs", tags=["Activity Log"])


@activity_log_router.get("/me/activity_log")
async def get_user_activity_logs(
    current_user: User = Depends(get_current_user),
    service: ActivityLogService = Depends(get_activity_log_service)
):
    response = await service.get_user_activity_logs(user_id=current_user.id)
    return response


@activity_log_router.get("/{activity_log_id}")
async def get_activity_log(
    activity_log_id: str,
    service: ActivityLogService = Depends(get_activity_log_service)
):
    response = await service.get_activity_log(activity_log_id)
    return response