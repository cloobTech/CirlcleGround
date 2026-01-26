from src.models.user import User
from src.model_schemas.user_schema import CreateUserSchema, ReadUser
from src.unit_of_work.unit_of_work import UnitOfWork
from src.core.exceptions import UserAlreadyExistsError
from src.enums.enums import UserRole
from src.auth.security import get_password_hash

class UserService:
    def __init__(self, uow_factory: UnitOfWork):
        self.uow_factory = uow_factory
    
    async def create_user(self, user_data: CreateUserSchema, role: UserRole):
        user = await self.uow_factory.user_repo.get_user_by_email(email=user_data.email)
        if user:
            raise UserAlreadyExistsError(message="Email already exists in database", details={
                "recommendation": "user should provide a different email"
            })
        
        data = user_data.model_dump()
        data["role"] = role
        data.pop("confirm_password")
        data['password'] = get_password_hash(user_data.password)
        user = User(**data)
        created_user = await self.uow_factory.user_repo.create(user)
        return ReadUser.model_validate(created_user)
    
    async def update_user(self, user_id: str, user_data):
        user = await self.uow_factory.user_repo.update(user_id, user_data)
        return ReadUser.model_validate(user)