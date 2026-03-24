from pydantic import BaseModel

class BaseReview(BaseModel):
    rating: float
    comment: str


class SendReviewSchema(BaseReview):
    # reviewee_id: str
    booking_id: str


class ReadReview(BaseReview):
    id: str
    reviewer_name: str
    reviewee_name: str

    
class UpdateReview(BaseReview):
    pass