from pydantic import BaseModel


class CreateBank(BaseModel):
    currency: str
    code: str
    name: str