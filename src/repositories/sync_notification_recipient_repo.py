from sqlalchemy.orm import Session
from sqlalchemy import select
from src.repositories.sync_base import SyncBaseRepository
from src.models.notification_recipient import NotificationRecipient


class NotificationRecipientRepository(SyncBaseRepository[NotificationRecipient]):
    def __init__(self, session: Session):
        super().__init__(NotificationRecipient, session)

    def get_by_notification_and_user(self, notification_id, recipient_id):

        result = self.session.execute(select(NotificationRecipient).where(
            NotificationRecipient.notification_id == notification_id,
            NotificationRecipient.recipient_id == recipient_id
 ))
        return result.scalar_one_or_none()

