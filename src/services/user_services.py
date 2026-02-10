from src.schemas.user_schema import ReadUser
from src.unit_of_work.unit_of_work import UnitOfWork


class UserService:
    def __init__(self, uow_factory: UnitOfWork):
        self.uow_factory = uow_factory

    async def update_user(self, user_id: str, user_data):
        async with self.uow_factory:
            user = await self.uow_factory.user_repo.update(id=user_id, data=user_data)
            return ReadUser.model_validate(user)
