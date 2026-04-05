from pydantic import BaseModel
from src.enums.enums import ActivityType


class ActivityLogSchema(BaseModel):
    activity: ActivityType
    user_id: str
    resource_type: str
    resource_id: str
    