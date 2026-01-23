from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from contextlib import asynccontextmanager
from src.models.basemodel import Base
from src.models import user, reviews, booking, payments, location, amenities, space, space_amenities
class Database:
    def __init__(self, db_url: str = "sqlite+aiosqlite:///mysqlalchemy.db"):
        self.__engine = create_async_engine(db_url, echo=False)
        self.__session_maker = async_sessionmaker(self.__engine, expire_on_commit=False)

    @asynccontextmanager
    async def get_session(self):
        async with self.__session_maker() as session:
            yield session

    async def create_table(self):
        """Creating a table in the database"""
        async with self.__engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    
    async def drop_tables(self):
        async with self.__engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)