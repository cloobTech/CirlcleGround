from src.models.basemodel import Base
from sqlalchemy import create_engine
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker


class SyncDBStorage:
    def __init__(self, db_url: str = "sqlite:///mysqlalchemy.db"):
        self.__engine = create_engine(db_url, echo=False)
        self.__session_maker = sessionmaker(
            self.__engine, expire_on_commit=False)

    @property
    def session_maker(self):
        return self.__session_maker

    @contextmanager
    def get_session(self):
        with self.__session_maker() as session:
            yield session
