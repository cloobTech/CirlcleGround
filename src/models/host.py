from models.base import Basemodel, Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import Optional

class Host(Basemodel, Base):
    __tablename__ = "hosts"

    user_id: Mapped[Optional[str]] = mapped_column(ForeignKey("users.id"), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    is_verified: Mapped[str] = mapped_column(default=False)
    

    user = relationship("User", back_populates="host")