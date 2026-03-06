from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.notification_recipient import NotificationRecipient


class NotificationRecipientRepository(BaseRepository[NotificationRecipient]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(NotificationRecipient, session)
