from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from src.models.basemodel import Base
from pydantic import EmailStr, BaseModel
from typing import Type, TypeVar, Generic, Dict, Union

ModelType = TypeVar("ModelType", bound=Base)

class BaseRepository(Generic[ModelType]):

    def __init__(self, model: Type[ModelType], session: AsyncSession):
        self.session = session
        self.model = model

    async def create(self, obj: ModelType):
        self.session.add(obj)
        return obj
    
    async def get_all(self):
        stmt = select(self.model)

        if hasattr(self.model, "is_deleted"):
            stmt = stmt.where(self.model.is_deleted == False)

        result = await self.session.scalars(stmt)
        return result.all()
    

    async def get_by_email(self, email: EmailStr):
        result = await self.session.execute(select(self.model).where(self.model.email == email))
        return result.scalar_one_or_none()

    async def get_by_id(self, id: str):
        result = await self.session.get(self.model, id)
        return result

    async def delete(self, id, soft: bool =False)-> bool:
        obj = await self.get_by_id(id)
        if not obj:
            return False
        
        if soft and hasattr(obj, "is_deleted"):
            setattr(obj, "is_deleted", True)
        else:
            await self.session.delete(obj)
        
        return True
    
    async def update(self, id: str, new_data):
        obj = await self.get_by_id(id)
        if not obj:
            return None

        IGNORE_LIST = {"id", "created_at", "updated_at"}

        for key, value in new_data.items():
            if key not in IGNORE_LIST:
                setattr(obj, key, value)

        return obj