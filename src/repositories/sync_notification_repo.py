from sqlalchemy.orm import Session
from src.models.notification import Notification
from src.schemas.notification import CreateNotification
from src.repositories.sync_base import SyncBaseRepository


class SyncNotificationRepository(SyncBaseRepository[Notification]):
    def __init__(self, session: Session):
        super().__init__(Notification, session)

    def create(self, obj: CreateNotification) -> Notification:
        notification = Notification(**obj.model_dump())
        return super().create(notification)
