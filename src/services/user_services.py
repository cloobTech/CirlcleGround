from models.user import User
from schemas.user_schema import CreateUserSchema

def create_user(user_data: CreateUserSchema):
    data = user_data.model_dump()
    user = User(**data)
