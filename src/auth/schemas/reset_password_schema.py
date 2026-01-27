from pydantic import BaseModel, Field

class ResetPasswordSchema(BaseModel):
    token: str = Field(..., description="Password reset token")
    password: str = Field(..., min_length=8)
    confirm_password: str
    