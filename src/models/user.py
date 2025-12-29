from models.base import Basemodel, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import Optional

class User(Basemodel, Base):
    __tablename__ ="users"

    full_name: Mapped[str] = mapped_column(String(250), nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_email_verfied: Mapped[bool] = mapped_column(default=False)
    reset_token: Mapped[str] = mapped_column(default=False, nullable=True)
    role: Mapped[str] = mapped_column()

    
    #relationships(One-many)
    customer: Mapped[Optional["Customer"]] = relationship(back_populates="user", uselist=False)
    # service_provider: Mapped[Optional["Service Provider"]] = relationship(back_populates="user", uselist=False)
    host: Mapped[Optional["Host"]] = relationship(back_populates="user", uselist=False)