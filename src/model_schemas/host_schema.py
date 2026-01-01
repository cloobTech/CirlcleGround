from pydantic import BaseModel



class CreateHostSchema(BaseModel):
    """Admin schema"""
    user_id : str
