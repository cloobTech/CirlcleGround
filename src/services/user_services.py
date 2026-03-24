from datetime import datetime, timezone
from src.schemas.user_schema import ReadUser, UpdateUserSchema
from src.schemas.booking_schema import BookingQueryParams
from src.schemas.space_schema import SpaceQueryParams
from src.unit_of_work.unit_of_work import UnitOfWork
from src.core.exceptions import EntityNotFound


class UserService:
    def __init__(self, uow_factory: UnitOfWork):
        self.uow_factory = uow_factory

    async def update_user(self, user_data: UpdateUserSchema, user_id: str):
        data = user_data.model_dump()
        async with self.uow_factory:
            user = await self.uow_factory.user_repo.update(user_id, data)
            return user_data

    async def get_user_spaces(self, user_id: str, params: SpaceQueryParams):
        async with self.uow_factory as uow:
            spaces = await uow.space_repo.get_user_spaces(user_id, params)
            return spaces

    async def get_user_bookings(self, guest_id: str, params: BookingQueryParams):
        async with self.uow_factory:
            return await self.uow_factory.booking_repo.get_user_bookings(guest_id, params)

    async def get_user_wishlist(self, user_id: str):
        async with self.uow_factory:
            return await self.uow_factory.wishlist_repo.list_user_wishlist(user_id)

    async def get_user_notifications(self, user_id: str):
        async with self.uow_factory:
            return await self.uow_factory.notification_repo.get_user_notifications(user_id)

    async def update_notification(self, notification_id: str, recipient_id: str):
        async with self.uow_factory as uow:
            notification_recipient = await uow.notification_recipient_repo.get_user_notification(notification_id, recipient_id)
            if not notification_recipient:
                raise EntityNotFound(
                    message="User notification not found",
                    details={
                        "recommendation": "Make sure you pass the correct notification and recipient ID"
                    }
                )
            await uow.notification_recipient_repo.update_user_notification(notification_recipient)
            return notification_recipient

    async def delete_user_notification(self, notification_id: str, recipient_id: str):
        async with self.uow_factory as uow:
            notification_recipient = await uow.notification_recipient_repo.get_user_notification(notification_id, recipient_id)
            if not notification_recipient:
                raise EntityNotFound(
                    message="User notification not found",
                    details={
                        "recommendation": "Make sure you pass the correct notification and recipient ID"
                    }
                )
            await uow.notification_recipient_repo.delete(notification_recipient.id)
            return {
                "message": "User's notification deleted"
            }

    async def delete_multiple_user_notifications(self, notification_ids: list[str], recipient_id: str):
        async with self.uow_factory as uow:
            notifications = await uow.notification_recipient_repo.get_multiple_user_notifications(notification_ids, recipient_id)
            if not notifications:
                raise EntityNotFound(
                    message="Notifications not found",
                    details={
                        "recommendation": "Ensure the notification IDs belong to the user"
                    }
                )
            await uow.notification_recipient_repo.delete_multiple_notifications(notification_ids, recipient_id)
            return {
                "message": "User's notifications successfully deleted",
                "deleted_rows": len(notifications)
            }

    async def get_user_conversations(self, user_id: str):
        async with self.uow_factory:
            conversations = await self.uow_factory.conversation_repo.get_user_conversations(user_id)

            user_ids = [c["other_user_id"] for c in conversations]
            users = await self.uow_factory.user_repo.get_multiple_users_by_ids(user_ids)
            user_map = {u.id: u for u in users}

        for conv in conversations:
            other_user_id = conv.pop("other_user_id", None)

            user = user_map.get(other_user_id)

            if user:
                conv["other_participant"] = {
                    "id": user.id,
                    "name": f"{user.first_name} {user.last_name}",
                    "avatar": user.profile_image
                }
            else:
                conv["other_participant"] = {
                    "id": None,
                    "name": "Unknown User",
                    "avatar": None
                }

        return conversations
