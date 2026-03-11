from src.schemas.notification import CreateNotification
from src.events.notification_events import NotificationCreatedEvent
from src.enums.enums import NotificationType

class SpaceNotificationFactory:
    
    @staticmethod
    def space_created(space, host_id: str):
        return NotificationCreatedEvent(
            data = CreateNotification(
                title="New Space Created",
                message=f"A new space '{space.name}' has been created by host {host_id}.",
                sender_id=host_id,
                notification_type=NotificationType.SPACE_CREATION,
                resource_id=space.id
            ),
            event_type="NOTIFICATION_CREATED",
            recipient_ids=[host_id]
        )
    

