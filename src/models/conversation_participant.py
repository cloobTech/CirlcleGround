from datetime import datetime
from src.models.basemodel import Basemodel, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.user import User
    from src.models.conversation import Conversation


class ConversationParticipant(Basemodel, Base):
    __tablename__ = "conversation_participants"

    conversation_id: Mapped[str] = mapped_column(
        ForeignKey("conversations.id"), primary_key=True
    )
    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"), primary_key=True
    )
    last_read_at: Mapped[datetime | None] = mapped_column(nullable=True)

    user: Mapped["User"] = relationship()
    conversation: Mapped["Conversation"] = relationship(
        back_populates="participants"
    )
