from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.booking_repo import BookingRepository
from src.repositories.payment_repo import PaymentRepository
from src.repositories.space_repo import SpaceRepository
from src.repositories.user_repo import UserRepository
from src.repositories.location_repo import LocationRepository
from src.repositories.amenity_repo import AmenityRepository
from src.repositories.custom_amenity_repo import CustomAmenityRepository
from src.repositories.space_rule import SpaceRuleRepository
from src.repositories.space_pricing_repo import SpacePricingRepository
from src.repositories.space_image_repo import SpaceImageRepository
from src.repositories.space_addon_repo import SpaceAddonRepository
from src.repositories.space_usecase_repo import SpaceUseCaseRepository
from src.repositories.space_amenity_repo import SpaceAmenityRepository
from src.repositories.booking_history_status_repo import BookingHistoryStatusRepository
from src.repositories.space_operating_hour_repo import SpaceOperatingHourRepository
from src.repositories.space_blackout_repo import SpaceBlackoutRepository
from src.repositories.booking_addon_repo import BookingAddonRepository
from src.repositories.wishlist_repo import WishListRepository
from src.repositories.notification_repo import NotificationRepository
from src.repositories.notification_recipient_repo import NotificationRecipientRepository
from src.repositories.conversation_repo import ConversationRepository
from src.repositories.message_repo import MessageRepository
from src.repositories.conversation_participant_repo import ConversationParticipantRepository
from src.repositories.review_repo import ReviewRepository

from src.events.bus import event_bus
from src.events.base import DomainEvent
from sqlalchemy.exc import IntegrityError
from src.core.exceptions import UniqueViolationError


class UnitOfWork:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.event_bus = event_bus
        self._pending_events: list[DomainEvent] = []

        self.user_repo = UserRepository(session)
        self.space_repo = SpaceRepository(session)
        self.booking_repo = BookingRepository(session)
        self.payment_repo = PaymentRepository(session)
        self.location_repo = LocationRepository(session)
        self.amenity_repo = AmenityRepository(session)
        self.custom_amenity_repo = CustomAmenityRepository(session)
        self.space_rule_repo = SpaceRuleRepository(session)
        self.space_pricing_repo = SpacePricingRepository(session)
        self.space_image_repo = SpaceImageRepository(session)
        self.space_addon_repo = SpaceAddonRepository(session)
        self.space_usecase_repo = SpaceUseCaseRepository(session)
        self.space_amenity_repo = SpaceAmenityRepository(session)
        self.booking_history_status_repo = BookingHistoryStatusRepository(
            session)
        self.space_operating_hour_repo = SpaceOperatingHourRepository(session)
        self.space_blackout_repo = SpaceBlackoutRepository(session)
        self.booking_addon_repo = BookingAddonRepository(session)
        self.wishlist_repo = WishListRepository(session)
        self.notification_repo = NotificationRepository(session)
        self.notification_recipient_repo = NotificationRecipientRepository(
            session)
        self.conversation_repo = ConversationRepository(session)
        self.message_repo = MessageRepository(session)
        self.conversation_participant_repo = ConversationParticipantRepository(
            session)
        self.review_repo = ReviewRepository(session)

    def collect_event(self, event: DomainEvent) -> None:
        # print(f"Collecting event: {event}")
        self._pending_events.append(event)

    async def __aenter__(self):
        await self.session.begin()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        try:
            if exc_type is not None:
                await self.session.rollback()
                self._pending_events.clear()
                await self.session.close()
                return False

            await self.session.commit()

        except IntegrityError as e:
            await self.session.rollback()
            self._pending_events.clear()
            raise UniqueViolationError() from e
        except Exception:
            await self.session.rollback()
            self._pending_events.clear()
            raise
        finally:
            await self.session.close()

        # publish only if event_bus exists
        if self.event_bus is not None:
            for ev in self._pending_events:
                await self.event_bus.publish(ev)

        self._pending_events.clear()
