from pydantic import BaseModel


class MessageSchema(BaseModel):
    content: str
    sender_id: str
    conversation_id: str


class UpdateMessageSchema(BaseModel):
    content: str
