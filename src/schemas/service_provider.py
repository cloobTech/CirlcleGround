from pydantic import BaseModel
from typing import Literal

class CreateServiceProviderSchema(BaseModel):
    """Admin schema"""
    skills: str
    preferred_location: str
    tools_needed: str
    