from models.user import User
from model_schemas.user_schema import CreateUserSchema
from unit_of_work.unit_of_work import UnitOfWork
from src.core.exceptions import UserAlreadyExistsError

class UserService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
    
    # async def create_user(self, user_data: CreateUserSchema):
    #     async with self.uow as uow:
    #         user = await uow.user_repo.get_user_by_email(email=user_data.email)
    #         if user:
    #             raise UserAlreadyExistsError(message="Email already exists in database", details={
    #                 "recommendation": "user should provide a different email"
    #             })
    #         user = User(**user_data.model_dump())
    #         created_user = await uow.user_repo.create(user)
    #         return created_user
        

            
