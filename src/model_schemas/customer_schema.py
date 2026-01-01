from pydantic import BaseModel



class CreateCustomerSchema(BaseModel):
    """Admin schema"""
    user_id: str
    preferred_location: str
    

    