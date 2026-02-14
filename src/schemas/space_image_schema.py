from pydantic import BaseModel

class DeleteSpaceImage(BaseModel):
    image_ids: list[str]