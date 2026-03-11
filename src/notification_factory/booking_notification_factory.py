from src.schemas.notification import CreateNotification
from src.events.notification_events import NotificationCreatedEvent
from src.enums.enums import NotificationType


class BookingNotificationFactory:

    @staticmethod
    def booking_requested(booking_id: str, guest_id: str, space: str, host_id: str):
        return NotificationCreatedEvent(
            data=CreateNotification(
                title="New Booking Request",
                message=f"A new booking request was made for '{space.name}'.",
                sender_id=guest_id,
                notification_type=NotificationType.BOOKING_REQUESTED,
                resource_id=booking_id
            ),
            event_type="NOTIFICATION_CREATED",
            recipient_ids=[host_id]
        )
    

    @staticmethod
    def booking_accepted(booking_id: str, guest_id: str, space: str, host_id: str):
        return NotificationCreatedEvent(
            data=CreateNotification(
                title="Booking Accepted",
                message=f"Your booking for '{space.name}' has been accepted.",
                sender_id=host_id,
                notification_type=NotificationType.BOOKING_REQUESTED,
                resource_id=booking_id
            ),
            event_type="NOTIFICATION_CREATED",
            recipient_ids=[guest_id]
        )
    
    @staticmethod
    def booking_declined(booking_id: str, guest_id: str, space: str, host_id: str):
        return NotificationCreatedEvent(
            data=CreateNotification(
                title="Booking Declined",
                message=f"Your booking for '{space.name}' has been declined.",
                sender_id=host_id,
                notification_type=NotificationType.BOOKING_REQUESTED,
                resource_id=booking_id
            ),
            event_type="NOTIFICATION_CREATED",
            recipient_ids=[guest_id]
        )
    
    @staticmethod
    def booking_confirmed(booking_id: str, guest_id: str, space: str, host_id: str):
        return NotificationCreatedEvent(
            data=CreateNotification(
                title="Booking Confirmed",
                message=f"Your booking for '{space.name}' has been confirmed",
                sender_id=host_id,
                notification_type=NotificationType.BOOKING_CONFIRMED,
                resource_id=booking_id
            ),
            event_type="NOTIFICATION_CREATED",
            recipient_ids=[guest_id]
        )
    
    @staticmethod
    def booking_cancelled(booking_id: str, guest_id: str, space: str, host_id: str):
        return NotificationCreatedEvent(
            data=CreateNotification(
                title="Booking Cancelled",
                message=f"Your booking for '{space.name}' has been confirmed",
                sender_id=guest_id,
                notification_type=NotificationType.BOOKING_CANCELLED,
                resource_id=booking_id
            ),
            event_type="NOTIFICATION_CREATED",
            recipient_ids=[host_id]
        )
    

    @staticmethod
    def booking_checkin_reminder(space, booking_id, host_id, guest_id, checkin_time):
        return NotificationCreatedEvent(
            data=CreateNotification(
                title="Check-in reminder",
                message=f"Booking for '{space.name}' starts at '{checkin_time}'.",
                sender_id=None,
                notification_type=NotificationType.BOOKING_CANCELLED,
                resource_id=booking_id
            ),
            event_type="NOTIFICATION_CREATED",
            recipient_ids=[host_id, guest_id]
        )
    

    @staticmethod
    def booking_checkout_reminder(space, booking_id, host_id, guest_id, checkin_time):
        return NotificationCreatedEvent(
            data=CreateNotification(
                title="Check-out reminder",
                message=f"Booking for '{space.name}' ends at '{checkin_time}'.",
                sender_id=None,
                notification_type=NotificationType.BOOKING_CANCELLED,
                resource_id=booking_id
            ),
            event_type="NOTIFICATION_CREATED",
            recipient_ids=[host_id, guest_id]
        )