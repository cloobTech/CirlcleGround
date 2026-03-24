from fastapi import APIRouter, Depends
from src.schemas.reviews_schema import SendReviewSchema, UpdateReview
from src.models.user import User
from src.api.v1.dependencies import get_current_user, get_review_service
from src.services.review_services import ReviewService


review_router = APIRouter(prefix="/api/v1/reviews", tags=["Reviews"])


@review_router.post("/")
async def send_review(
    review_data: SendReviewSchema,
    user: User = Depends(get_current_user),
    review_service: ReviewService = Depends(get_review_service)
):
    response = await review_service.send_review(review_data, reviewer_id=user.id)
    return response


@review_router.patch("/{review_id}")
async def update_review(
    review_id: str,
    review_data: UpdateReview,
    user: User = Depends(get_current_user),
    review_service: ReviewService = Depends(get_review_service)
):
    response = await review_service.update_review(review_id, review_data, user_id=user.id)
    return response


@review_router.get("/{space_id}")
async def get_space_reviews(
    space_id: str,
    review_service: ReviewService = Depends(get_review_service)
):
    response = await review_service.get_space_reviews(space_id)
    return response

@review_router.delete("/{review_id}")
async def delete_review(
    review_id: str,
    review_service: ReviewService = Depends(get_review_service)
):
    response = await review_service.delete_review(review_id)
    return response


@review_router.delete("/{space_id}/reviews")
async def delete_space_review(
    space_id: str,
    review_service: ReviewService = Depends(get_review_service)
):
    response = await review_service.delete_space_reviews(space_id)
    return response

