from src.events.message_events import MessageCreatedEvent
from src.events.connections.websocket_manager import manager


async def handle_message_created_event(event: MessageCreatedEvent):
    # Broadcast the new message to all connected WebSocket clients
    await manager.send_to_users(event.recipient_ids, {
        "message": {
            "id": event.message.id,
            "content": event.message.content,
            "sender_id": event.message.sender_id,
            "conversation_id": event.message.conversation_id,

        }
    })
