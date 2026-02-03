from src.models.user import User
from src.model_schemas.user_schema import CreateUserSchema, ReadUser
from src.unit_of_work.unit_of_work import UnitOfWork
from src.core.exceptions import UserAlreadyExistsError
from src.enums.enums import UserRole
from src.auth.security import hash_password
from src.utils.email_service import email_service
from src.utils.email_templates import verify_email_template

class UserService:
    def __init__(self, uow_factory: UnitOfWork):
        self.uow_factory = uow_factory
    
    async def update_user(self, user_id: str, user_data):
        async with self.uow_factory:
            user = await self.uow_factory.user_repo.update(user_id, user_data)
            return ReadUser.model_validate(user)