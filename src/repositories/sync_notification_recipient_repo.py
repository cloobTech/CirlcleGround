from sqlalchemy.orm import Session
from sqlalchemy import select
from src.repositories.sync_base import SyncBaseRepository
from src.models.notification_recipient import NotificationRecipient


class NotificationRecipientRepository(SyncBaseRepository[NotificationRecipient]):
    def __init__(self, session: Session):
        super().__init__(NotificationRecipient, session)
