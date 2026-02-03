from pydantic import BaseModel

class TokenResponse(BaseModel):
    """Token Response"""
    message: str = "Login successful"
    token: str
    token_type: str = "Bearer"