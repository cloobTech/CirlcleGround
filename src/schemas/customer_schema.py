from pydantic import BaseModel
from typing import Literal

class CreateCustomerSchema(BaseModel):
    """Admin schema"""
    preferred_location: str
    tools_needed: str
    