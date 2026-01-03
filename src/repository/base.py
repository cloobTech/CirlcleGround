from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from models.base import Base
from pydantic import EmailStr
from typing import Type, TypeVar, Generic

ModelType = TypeVar("ModelType", bound=Base)

class BaseRepository(Generic[ModelType]):

    def __init__(self, model: Type[ModelType], session: AsyncSession):
        self.session = session
        self.model = model

    async def create(self, obj: ModelType):
        self.session.add(obj)
        return obj
    
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
    
    async def get_all(self):
        stmt = select(self.model)

        if hasattr(self.model, "is_deleted"):
            stmt = stmt.where(self.model.is_deleted == False)

        result = await self.session.scalars(stmt)
        return result.all()
    
    async def update(self, id: str, data: dict):
        if not data:
            return None

        obj = await self.get_by_id(id)
        if not obj:
            return None

        IGNORE_LIST = {"id", "created_at", "updated_at"}

        for key, value in data.items():
            if key not in IGNORE_LIST:
                setattr(obj, key, value)

        return obj

        






    # def add(self, session: AsyncSession, obj):
    #     session.add(obj)
    
    # async def save(self, session: AsyncSession, obj = None):
    #     if obj:
    #         self.add(session, obj)
    #     await session.commit()CVBNM
    
    # async def get_by_class(self, session: AsyncSession, model: Base):
    #     smtp = select(model)
    #     result = await session.execute(smtp)
    #     return result.scalars().all()
    
    # async def get_by_id(self, session: AsyncSession, cls: Base, object_id:str):
    #     result = await session.execute(select(cls).where(cls.id == object_id))
    #     return result.scalar_one_or_none()
    

    # async def get_by_column_name(self, session: AsyncSession, cls: Base, column_name: str):
    #     column = getattr(cls, column_name,  None)
    #     if column is None:
    #         return (f"{column_name} not found in db")
    #     smtp = await session.execute(select(column))
    #     result = [row[0] for row in smtp.all()]
    #     return result
    
    # async def update_info(self, session: AsyncSession, cls: Base, id: str, key: str, value):
    #     result = await self.get_by_id(session, cls, id)
    #     if not result:
    #         return ("Record not found in db")
    #     setattr(result, key, value)
    #     await session.commit()
    #     return result
    
    # async def get_by_user_id(self, session: AsyncSession, cls: Base, user_id: str):
    #     result = await session.execute(select(cls).where(cls.user_id == user_id))
    #     return result.scalars().first()
    
    # async def delete_by_id(self, session: AsyncSession, cls: Base, id: str):
    #     result = await self.get_by_id(session, cls, id)
    #     if not  result:
    #         return (f"{cls.__name__} with {id} not in DB")
    #     await session.delete(result)
    #     await session.commit()
    #     return result
    
    
    # async def get_by_email(self, session, cls: Base, email: EmailStr):
    #     result = await session.execute(select(cls).where(cls.email == email))
    #     return result.scalar_one_or_none()
    
    # async def verify(self, session: AsyncSession, cls: Base, token):
    #     result = await session.execute(select(cls).where(cls.reset_token == token))
    #     return result