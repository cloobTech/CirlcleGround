import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from src.storage import db

from src.services.super_admin_services import SuperAdminService
from src.model_schemas.user_schema import CreateUserSchema, ReadUser
from src.enums.enums import UserRole
from src.auth.security import get_password_hash
from src.api.v1.dependencies import get_session, get_uow
from src.models.user import User
from src.unit_of_work.unit_of_work import UnitOfWork
from src.core.exceptions import UserAlreadyExistsError


async def main():
    async_session = db.session_maker()
    async with async_session as session:
        async with get_uow(session) as uow:
            service = SuperAdminService(uow)
            super_admin = await service.create_first_super_admin()
            print(super_admin)


if __name__ == "__main__":
    asyncio.run(main())
