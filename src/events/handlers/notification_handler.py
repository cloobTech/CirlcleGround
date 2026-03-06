from src.events.notification_events import NotificationCreatedEvent
from src.tasks.notification_task import create_notification


async def handle_notification_created(event: NotificationCreatedEvent):

    assert isinstance(event, NotificationCreatedEvent)
    notification_data = event.data
    recipient_ids = event.recipient_ids

    return create_notification.delay(notification_data=notification_data.model_dump(),
                                     recipient_ids=recipient_ids)
