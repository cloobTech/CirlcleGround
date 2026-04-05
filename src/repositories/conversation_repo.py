from sqlalchemy import select, func, and_
from sqlalchemy.orm import aliased
from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.conversation import Conversation
from src.models.message import Message
from src.models.conversation_participant import ConversationParticipant


class ConversationRepository(BaseRepository[Conversation]):
    def __init__(self, session: AsyncSession):
        super().__init__(Conversation, session)

    async def create_conversation(self) -> Conversation:
        conversation = Conversation()
        await self.create(conversation)
        return conversation

    async def get_conversation_by_chat_key(self, chat_key: str) -> Conversation | None:
        return await self.session.scalar(
            select(Conversation).where(
                Conversation.direct_chat_key == chat_key)
        )

    async def get_user_conversations(self, user_id: str):
        cp = ConversationParticipant
        msg = Message

        other_cp = aliased(ConversationParticipant) 

        # Ranked messages
        ranked_msg_subq = (
            select(
                msg.conversation_id,
                msg.content.label("last_message"),
                msg.created_at.label("last_message_at"),
                func.row_number()
                    .over(
                        partition_by=msg.conversation_id,
                        order_by=[msg.created_at.desc(), msg.id.desc()]
                )
                .label("rn")
            )
            .subquery()
        )

        # Unread count
        unread_subq = (
            select(
                msg.conversation_id,
                func.count(msg.id).label("unread_count")
            )
            .join(cp, cp.conversation_id == msg.conversation_id)
            .where(
                cp.user_id == user_id,
                msg.created_at > func.coalesce(cp.last_read_at, '1970-01-01')
            )
            .group_by(msg.conversation_id)
            .subquery()
        )

        stmt = (
            select(
                cp.conversation_id,
                ranked_msg_subq.c.last_message,
                ranked_msg_subq.c.last_message_at,
                func.coalesce(unread_subq.c.unread_count,
                              0).label("unread_count"),
                other_cp.user_id.label("other_user_id") 
            )
            .join(
                ranked_msg_subq,
                and_(
                    ranked_msg_subq.c.conversation_id == cp.conversation_id,
                    ranked_msg_subq.c.rn == 1
                )
            )
            .outerjoin(
                unread_subq,
                unread_subq.c.conversation_id == cp.conversation_id
            )
            .join(
                other_cp,
                and_(
                    other_cp.conversation_id == cp.conversation_id,
                    other_cp.user_id != user_id
                )
            )
            .where(cp.user_id == user_id)
            .order_by(ranked_msg_subq.c.last_message_at.desc())
        )

        result = await self.session.execute(stmt)

        return [
            {
                "conversation_id": row.conversation_id,
                "last_message": row.last_message,
                "last_message_at": row.last_message_at,
                "unread_count": row.unread_count,
                "other_user_id": row.other_user_id 
            }
            for row in result
        ]
