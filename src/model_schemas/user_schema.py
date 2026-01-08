from pydantic import BaseModel, EmailStr, model_validator
from typing import Literal


class CreateUserSchema(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    password: str
    confirm_password: str
    location: str
    role: Literal["host", "guest"]

    @model_validator(mode='before')
    def normalize_case(cls, dict_value):
        """ To change the values to lower case before validation"""
        for field in ['role']:
            if field in dict_value and isinstance(dict_value[field], str):
                dict_value[field] = dict_value[field].lower()
        return dict_value
    
    @model_validator(mode="before")
    def passwords_match(cls, values):
        password = values.get("password")
        confirm_password = values.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise ValueError("Passwords do not match")
        return values
    


class UserLoginSchema(BaseModel):
    identifier: str
    password: str
