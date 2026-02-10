from pydantic import BaseModel


class SendReviewSchema(BaseModel):
    user_id: str
    space_id: str
    comment: str