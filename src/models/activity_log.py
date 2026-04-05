from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING
from src.models.basemodel import Basemodel, Base

if TYPE_CHECKING:
    from src.models.user import User

class ActivityLog(Basemodel, Base):
    __tablename__="activity_logs"

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    activity: Mapped[str] = mapped_column(nullable=False)
    resource_type: Mapped[str] = mapped_column(nullable=False)
    resource_id: Mapped[str] = mapped_column(nullable=False)
    
