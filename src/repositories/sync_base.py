from datetime import datetime, timezone
from sqlalchemy.orm import Session
from sqlalchemy import select, update
from src.models.basemodel import Base
from typing import Type, TypeVar, Generic

ModelType = TypeVar("ModelType", bound=Base)


class SyncBaseRepository(Generic[ModelType]):

    def __init__(self, model: Type[ModelType], session: Session):
        self.session = session
        self.model = model
        self.supports_soft_delete = hasattr(model, "is_deleted")

    def create(self, obj: ModelType):
        self.session.add(obj)
        return obj

    def bulk_create(self, objs: list[ModelType]):
        self.session.add_all(objs)
        return objs

    def get_all(self, include_deleted: bool = False) -> list[ModelType]:
        stmt = select(self.model)
        if self.supports_soft_delete and not include_deleted:
            stmt = stmt.where(self.model.is_deleted == False)  # type: ignore
        result = self.session.scalars(stmt)
        return list(result.all())

    def get_by_id(self, id: str):
        result = self.session.get(self.model, id)
        return result

    def delete(self, id, soft: bool = False) -> bool:
        obj = self.get_by_id(id)
        if not obj:
            return False

        if soft and self.supports_soft_delete:
            setattr(obj, "is_deleted", True)
            setattr(obj, "deleted_at", datetime.now(timezone.utc))
        else:
            self.session.delete(obj)

        return True

    def restore(self, obj: ModelType) -> ModelType:
        if self.supports_soft_delete:
            setattr(obj, "is_deleted", True)
            if hasattr(obj, "deleted_at"):
                setattr(obj, "deleted_at", None)
            self.session.add(obj)
        return obj

    def get_deleted(self) -> list[ModelType]:
        """Return only soft-deleted objects"""
        if not self.supports_soft_delete:
            return []
        stmt = select(self.model).where(
            self.model.is_deleted == True)  # type: ignore
        result = self.session.scalars(stmt)
        return list(result.all())

    def update(self, id: str, filters: dict | None = None, data: dict | None = None) -> bool:
        if not data:
            return False

        IGNORE_LIST = [
            'id', 'created_at', 'updated_at'
        ]
        updated_dict = {}
        if data:
            updated_dict = {
                key: value for key, value in data.items() if key not in IGNORE_LIST
            }

        stmt = update(self.model).values(**updated_dict)
        if id:
            stmt = stmt.where(getattr(self.model, "id") == id)
        elif filters:
            stmt = stmt.filter_by(**filters)
        else:
            raise ValueError(
                "You must provide either id or filters to update.")

        result = self.session.execute(stmt)
        return True
