from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.notification import Notification
from src.models.notification_recipient import NotificationRecipient
from sqlalchemy import select, and_


class NotificationRepository(BaseRepository[Notification]):
    def __init__(self, session: AsyncSession):
        super().__init__(Notification, session)

    async def get_user_notifications(self, user_id: str):
        stmt = (
            select(Notification)
            .join(NotificationRecipient, NotificationRecipient.notification_id == Notification.id)
            .where(NotificationRecipient.recipient_id == user_id)
            .order_by(Notification.created_at.desc())
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()
