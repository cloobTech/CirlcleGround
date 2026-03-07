from datetime import datetime, timezone
from src.models.notification_recipient import NotificationRecipient
from src.unit_of_work.sync_uow import SyncUnitOfWork
from src.core.exceptions import EntityNotFound


class SyncNotificationRecipientService:
    def __init__(self, uow_factory: SyncUnitOfWork):
        self.uow_factory = uow_factory

    def update_notification(self, notification_id: str, recipient_id: str):
        with self.uow_factory as uow:
            recipient_notification = uow.sync_notification_recipient_repo.get_by_notification_and_user(notification_id, recipient_id)
            if not recipient_notification:
                raise EntityNotFound(
                    message="User notification not found",
                    details={
                        "recommendation": "Make sure you pass the correct notification and recipient ID"
                    }
                )
            recipient_notification.is_read = True
            recipient_notification.read_at = datetime.now(timezone.utc)
            return recipient_notification
    
    def delete_user_notification(self, notification_id: str, recipient_id: str):
        with self.uow_factory as uow:
            recipient_notification = uow.sync_notification_recipient_repo.get_by_notification_and_user(notification_id, recipient_id)
            if not recipient_notification:
                raise EntityNotFound(
                    message="User notification not found",
                    details={
                        "recommendation": "Make sure you pass the correct notification and recipient ID"
                    }
                )
            uow.sync_notification_recipient_repo.delete(recipient_notification.id)
            return {
                "message": "User's notification deleted",
            }
