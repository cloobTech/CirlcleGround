from src.models.user import User
from src.unit_of_work.unit_of_work import UnitOfWork
from src.schemas.user_schema import ReadUser, CreateUserSchema
from src.auth.services import AuthService
from src.enums.enums import UserRole
from src.core.exceptions import UserAlreadyExistsError
from src.auth.security import hash_password


class SuperAdminService:
    def __init__(self, uow_factory: UnitOfWork):
        self.uow_factory = uow_factory
        self.auth_service = AuthService(uow_factory)

    async def create_first_super_admin(self, background_tasks):
        user_data = CreateUserSchema(
            first_name="Emmanuel",
            last_name="Nwokoma",
            email="emmanuelnwokoma364@gmail.com",
            phone_number="09038457350",
            password="1234567890",
            confirm_password="1234567890",
            location="kano"

        )
        exisiting_user = await self.uow_factory.user_repo.get_user_by_email(user_data.email)

        existing_super_admin = await self.uow_factory.user_repo.get_super_admin()

        if existing_super_admin or exisiting_user:
            raise UserAlreadyExistsError()

        super_admin = await self.auth_service.create_user(user_data, background_tasks, role=UserRole.SUPER_ADMIN)
        return ReadUser.model_validate(super_admin)
