from datetime import datetime, timedelta, timezone
from src.unit_of_work.unit_of_work import UnitOfWork
from src.schemas.reviews_schema import SendReviewSchema, ReadReview, UpdateReview
from src.enums.enums import ReviewType, BookingStatus
from src.core.pydantic_confirguration import config
from src.core.exceptions import EntityNotFound, PermissionDeniedError, EntityAlreadyExist
from src.models.reviews import Review
from src.models.user import User


class ReviewService:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory

    
    
    async def send_review(self, review_data: SendReviewSchema, reviewer_id: str):
        async with self.uow_factory:
            user = await self.uow_factory.user_repo.get_by_id(reviewer_id)
            if not user:
                raise EntityNotFound(
                    message="User not found",
                    details={
                        "recommendation": "Pass the correct user id"
                    }
                )
            booking = await self.uow_factory.booking_repo.get_booking(review_data.booking_id)
            if not booking:
                raise EntityNotFound(
                    message="Booking not found",
                    details={
                        "recommendation": "Pass the correct booking id"
                    }
                )
            if booking.status != BookingStatus.COMPLETED:
                raise ValueError("Booking must be completed")
            
            if booking.guest_id == reviewer_id:
                review_type = ReviewType.GUEST_USER_TO_SPACE
                reviewee_id = booking.space.host_id
            
            elif booking.space.host_id == reviewer_id:
                review_type = ReviewType.HOST_TO_GUEST_USER
                reviewee_id = booking.guest_id

            else:
                raise PermissionDeniedError(
                    message="You must have completed a booking to review space",
                    details={
                        "recommendation": "Pass the correct user_id"
                    }
                )
            existing_review = await self.uow_factory.review_repo.get_booking_review(review_data.booking_id, reviewer_id)
            if existing_review:
                raise EntityAlreadyExist(
                    message="You have reviewed this space"
                )
            data = review_data.model_dump()
            data["reviewer_id"] = reviewer_id
            data["reviewee_id"] = reviewee_id
            data["review_type"] = review_type
            data["space_id"] = booking.space_id

            review = Review(**data)
            
            new_review = await self.uow_factory.review_repo.create(review)
            reviewer = await self.uow_factory.user_repo.get_by_id(reviewer_id)
            reviewer_name = f"{reviewer.first_name}" + " " f"{reviewer.last_name}"
            reviewee = await self.uow_factory.user_repo.get_by_id(reviewee_id)
            reviewee_name = f"{reviewee.first_name}" + " " + f"{reviewee.last_name}"
            return ReadReview(
                reviewer_name=reviewer_name,
                reviewee_name= reviewee_name,
                comment= new_review.comment,
                rating=new_review.rating
            )
         

    async def update_review(self, review_id: str, review_data: UpdateReview, user_id: str):
        async with self.uow_factory:
            update_window = datetime.now(timezone.utc) + (timedelta(minutes=config.UPDATE_WINDOW_MINUTES))
            user = await self.uow_factory.user_repo.get_by_id(user_id)
            if not user:
                raise EntityNotFound(
                    message="User not found",
                    details={
                        "recommendation": "Pass the correct user id"
                    }
                )
            review = await self.uow_factory.review_repo.get_review(review_id)
            if not review:
                raise EntityNotFound(
                    message="Review not found",
                    details={
                        "recommendation": "Pass the correct review id"
                    }
                )
            if review.reviewer_id != user_id:
                raise PermissionDeniedError(
                    message="You do not have permission to update this review",
                    details={
                        "recommendation": "Make sure the reviwer_id is same as the user_id"
                    }
                )
            if datetime.now(timezone.utc) >= update_window:
                raise PermissionDeniedError(
                    message="Update window expired",
                    details={
                        "recommendation": "Make sure update window is still open"
                    }
                )
            
            data = review_data.model_dump()
            
            updated_review = await self.uow_factory.review_repo.update(id=review_id, data=data)
            
            return updated_review

    
    async def get_space_reviews(self, space_id: str):
        async with self.uow_factory:
            reviews = await self.uow_factory.review_repo.get_space_reviews(space_id)
            overall_rating = await self.uow_factory.review_repo.get_space_rating(space_id)

          

            read_reviews = []
            for review in reviews:
                reviewer_name = f"{review.reviewer.first_name}  {review.reviewer.last_name}"
                reviewee_name = f"{review.reviewee.first_name} {review.reviewee.last_name}"
                read_reviews.append(
                    ReadReview(
                        reviewer_name=reviewer_name,
                        reviewee_name=reviewee_name,
                        comment=review.comment,
                        rating=review.rating,
                       
                    )
                )
            return {
                "reviews": read_reviews,
                "overall_rating": overall_rating
            }
    
    async def delete_review(self, review_id: str):
        async with self.uow_factory:
            review = await self.uow_factory.review_repo.get_by_id(review_id)
            if not review:
                raise EntityNotFound(
                    message="Review not found",
                    details={
                        "recommendation": "Pass the correct review id"
                    }
                )
            deleted_review = await self.uow_factory.review_repo.delete(review_id, soft=True)
            return deleted_review

    async def delete_space_reviews(self, space_id: str):
        async with self.uow_factory:
            deleted_space_review = await self.uow_factory.review_repo.delete_space_reviews(space_id, soft=True)
            return deleted_space_review