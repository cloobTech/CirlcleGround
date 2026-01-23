from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.booking_repo import BookingRepository
from src.repositories.payment_repo import PaymentRepository
from src.repositories.space_repo import SpaceRepository
from src.repositories.user_repo import UserRepository
from src.repositories.location_repo import LocationRepository

class UnitOfWork:
    def __init__(self, session: AsyncSession):
        self.session = session

        self.user_repo = UserRepository(session)
        self.space_repo = SpaceRepository(session)
        self.booking_repo = BookingRepository(session)
        self.payment_repo = PaymentRepository(session)
        self.location_repo = LocationRepository(session)

    
    async def __aenter__(self):
        await self.session.begin()
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        if exc_type is not None:
            await self.session.rollback()
        else:
            await self.session.commit()