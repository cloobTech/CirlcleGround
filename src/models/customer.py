from models.base import Basemodel, Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey
from typing import Optional

class Customer(Basemodel, Base):
    __tablename__ = "customers"

    user_id: Mapped[Optional[str]] = mapped_column(ForeignKey("users.id"), nullable=False, unique=True)
    preferred_location: Mapped[str] = mapped_column(String(250), nullable=False)

    
    user = relationship("User", back_populates="customer")
    