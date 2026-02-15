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
from src.events.bus import event_bus
from src.events.base import DomainEvent


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

    def collect_event(self, event: DomainEvent) -> None:
        self._pending_events.append(event)

    async def __aenter__(self):
        # await self.session.begin()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        try:
            if exc_type is not None:
                await self.session.rollback()
                self._pending_events.clear()
                await self.session.close()
                return

            await self.session.commit()
        # except IntegrityError as e:
        #     print(exc_type, exc, tb)
        #     await self.session.rollback()
        #     self._pending_events.clear()
        #     raise UniqueViolationError("Duplicate record") from e
        except Exception:
            print(exc_type, exc, tb)
            print("rollback")
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
