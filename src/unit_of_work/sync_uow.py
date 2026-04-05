from sqlalchemy.orm import Session
from src.repositories.sync_notification_repo import SyncNotificationRepository
from src.repositories.sync_notification_recipient_repo import NotificationRecipientRepository
from src.events.bus import event_bus
from src.events.base import DomainEvent
from sqlalchemy.exc import IntegrityError
from src.core.exceptions import UniqueViolationError


class SyncUnitOfWork:
    def __init__(self, session: Session):
        self.session = session
        self.event_bus = event_bus
        self._pending_events: list[DomainEvent] = []

        self.sync_notification_repo = SyncNotificationRepository(session)
        self.sync_notification_recipient_repo = NotificationRecipientRepository(
            session)

    def collect_event(self, event: DomainEvent) -> None:
        self._pending_events.append(event)

    def __enter__(self):
        self.session.begin()
        return self

    def __exit__(self, exc_type, exc, tb):
        try:
            if exc_type is not None:
                self.session.rollback()
                self._pending_events.clear()
                self.session.close()
                return False

            self.session.commit()

        except IntegrityError as e:
            self.session.rollback()
            self._pending_events.clear()
            raise UniqueViolationError() from e
        except Exception:
            self.session.rollback()
            self._pending_events.clear()
            raise
        finally:
            self.session.close()

        # publish only if event_bus exists
        if self.event_bus is not None:
            for ev in self._pending_events:
                self.event_bus.publish_sync(ev)

        self._pending_events.clear()
