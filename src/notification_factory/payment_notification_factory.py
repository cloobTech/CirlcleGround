from src.schemas.notification import CreateNotification
from src.events.notification_events import NotificationCreatedEvent
from src.enums.enums import NotificationType



class PaymentNotificationFactory:

    @staticmethod
    def payment_success(booking_id: str, space: str, amount: float, guest_id: str, host_id: str):
        return NotificationCreatedEvent(
            data=CreateNotification(
                title="PAYMENT SUCCESSFUL",
                message=f"Payment of '{amount}' for '{space.name}' was succesuful.",
                sender_id=None,
                notification_type=NotificationType.PAYMENT_SUCCESS,
                resource_id=booking_id
            ),
            event_type="NOTIFICATION_CREATED",
            recipient_ids=[guest_id, host_id]
        )
    
    @staticmethod
    def payment_failed(booking_id: str, space: str, amount: float, guest_id: str, host_id: str):
        return NotificationCreatedEvent(
            data=CreateNotification(
                title="PAYMENT FAILED",
                message=f"Payment of '{amount}' for '{space.name}' has failed.",
                sender_id=None,
                notification_type=NotificationType.PAYMENT_FAILED,
                resource_id=booking_id
            ),
            event_type="NOTIFICATION_CREATED",
            recipient_ids=[guest_id, host_id]
        )