from pydantic import BaseModel, EmailStr, model_validator
from typing import Literal


class CreateUserSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    role: Literal["customer, service provider"]

    @model_validator(mode='before')
    def normalize_case(cls, dict_value):
        """ To change the values to lower case before validation"""
        for field in ['role']:
            if field in dict_value and isinstance(dict_value[field], str):
                dict_value[field] = dict_value[field].lower()
        return dict_value
