from sqlalchemy.orm import Session
from src.repositories.notification_repo import NotificationRepository
from src.repositories.notification_recipient_repo import NotificationRecipientRepository
from src.repositories.conversation_repo import ConversationRepository
from src.repositories.message_repo import MessageRepository
from src.repositories.conversation_participant_repo import ConversationParticipantRepository

from src.events.bus import event_bus
from src.events.base import DomainEvent
from sqlalchemy.exc import IntegrityError
from src.core.exceptions import UniqueViolationError


class SyncUnitOfWork:
    def __init__(self, session: Session):
        self.session = session
        self.event_bus = event_bus
        self._pending_events: list[DomainEvent] = []

        # self.notification_repo = NotificationRepository(session)
        # self.notification_recipient_repo = NotificationRecipientRepository(
        #     session)
        # self.conversation_repo = ConversationRepository(session)
        # self.message_repo = MessageRepository(session)
        # self.conversation_participant_repo = ConversationParticipantRepository(
        #     session)

    def collect_event(self, event: DomainEvent) -> None:
        self._pending_events.append(event)

    def __aenter__(self):
        self.session.begin()
        return self

    async def __aexit__(self, exc_type, exc, tb):
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
                await self.event_bus.publish(ev)

        self._pending_events.clear()
