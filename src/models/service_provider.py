from models.base import Basemodel, Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum as SAEnum
from enum import Enum

class ActiveStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class ServiceProvider(Basemodel, Base):
    skills: Mapped[str] = mapped_column(String(50), nullable=False)
    is_active: Mapped[str ]= mapped_column(SAEnum(ActiveStatus), default=ActiveStatus.INACTIVE)
    preferred_location: Mapped[str] = mapped_column(String(250), nullable=False)
    tools_needed: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[str] = mapped_column(nullable=False)
