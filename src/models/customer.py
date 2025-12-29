from models.base import Basemodel, Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey
from typing import Optional

class Customer(Basemodel, Base):
    __tablename__ = "customers"

    user_id: Mapped[Optional[str]] = mapped_column(ForeignKey("users.id"))
    preferred_location: Mapped[str] = mapped_column(String(250))

    
    user = relationship("User", back_populates="customer")
    