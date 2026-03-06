from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text, Index
from src.models.basemodel import Basemodel, Base, SoftDeleteMixin

if TYPE_CHECKING:
    from src.models.user import User
    from src.models.conversation import Conversation


class Message(Basemodel, Base, SoftDeleteMixin):
    __tablename__ = "messages"
    __table_args__ = (Index("ix_messages_conversation_created",
                      "conversation_id", "created_at"),)

    sender_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"), nullable=False)
    conversation_id: Mapped[str] = mapped_column(
        ForeignKey("conversations.id"), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    is_edited: Mapped[bool] = mapped_column(default=False)

    sender: Mapped["User"] = relationship()
    conversation: Mapped["Conversation"] = relationship(
        back_populates="messages"
    )
