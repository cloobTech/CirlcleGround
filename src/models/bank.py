from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from src.models.basemodel import Basemodel, Base




class Bank(Basemodel, Base):
    __tablename__="banks"
    currency: Mapped[str] = mapped_column(nullable=False)
    code: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)