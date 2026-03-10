from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from datetime import datetime, timezone
from src.repositories.base import BaseRepository
from src.models.notification_recipient import NotificationRecipient


class NotificationRecipientRepository(BaseRepository[NotificationRecipient]):
    def __init__(self, session: Session):
        super().__init__(NotificationRecipient, session)

    async def get_user_notification(self, notification_id, recipient_id):

        result = await self.session.execute(select(NotificationRecipient).where(
            NotificationRecipient.notification_id == notification_id,
            NotificationRecipient.recipient_id == recipient_id
 ))
        return result.scalar_one_or_none()
    

    async def get_multiple_user_notifications(self, notification_ids: list[str], recipient_id: str):
        result = await self.session.execute(
            select(NotificationRecipient).where(
                NotificationRecipient.notification_id.in_(notification_ids),
                NotificationRecipient.recipient_id == recipient_id
            )
        )
        return result.scalars().all()

    async def update_user_notification(self, notification_recipient: NotificationRecipient):
        notification_recipient.is_read = True
        notification_recipient.read_at = datetime.now(timezone.utc)
    
    async def delete_multiple_notifications(self, notification_ids: list[str], recipient_id: str):
        await self.session.execute(
            delete(NotificationRecipient).where(
                NotificationRecipient.notification_id.in_(notification_ids),
                NotificationRecipient.recipient_id == recipient_id
            )
        )  



