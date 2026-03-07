from fastapi import APIRouter, Depends
from src.models.user import User
from src.api.v1.dependencies import get_current_user, get_notification_recipient_service
from src.services.sync_notification_recipients import SyncNotificationRecipientService



notification_recipient_router = APIRouter(prefix="/api/v1/notification_recipient", tags=["Recipient Notification"])

@notification_recipient_router.patch("/{notification_id}/update-notification")
def update_user_notification(
    notification_id: str,
    current_user: User = Depends(get_current_user),
    service: SyncNotificationRecipientService = Depends(get_notification_recipient_service)
):

    recipient_notification = service.update_notification(
        notification_id=notification_id,
        recipient_id=current_user.id
    )
    return recipient_notification

@notification_recipient_router.delete("/{notification_id}")
def delete_user_notification(
    notification_id: str,
    current_user: User = Depends(get_current_user),
    service: SyncNotificationRecipientService = Depends(get_notification_recipient_service)
):
    deleted_recipient_notification = service.delete_user_notification(notification_id, recipient_id=current_user.id)
    return deleted_recipient_notification

