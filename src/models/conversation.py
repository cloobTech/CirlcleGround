from typing import TYPE_CHECKING
from src.models.basemodel import Basemodel, Base
from sqlalchemy.orm import Mapped,  relationship

if TYPE_CHECKING:
    from src.models.conversation_participant import ConversationParticipant
    from src.models.message import Message


class Conversation(Basemodel, Base):
    __tablename__ = "conversations"

    participants: Mapped[list["ConversationParticipant"]] = relationship(
        back_populates="conversation",
        cascade="all, delete-orphan"
    )
    messages: Mapped[list["Message"]] = relationship(
        back_populates="conversation"
    )
