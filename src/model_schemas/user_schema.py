from pydantic import BaseModel, EmailStr, model_validator
from typing import Literal
import phonenumbers
from src.core.exceptions import InvalidCredentialsError
from phonenumbers.phonenumberutil import NumberParseException


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
    
    @model_validator(mode="before")
    def phone_number_format(cls, values):
        phone_number = values.get("phone_number")
        if phone_number:
            try:
                num = phonenumbers.parse(phone_number, "NG")
                if phonenumbers.is_valid_number(num):
                    values["phone_number"] = phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.E164)
            except NumberParseException:
                raise InvalidCredentialsError(
                    details={"recommendations": "Phone number could not be parsed"}
                )
        return values


class UserLoginSchema(BaseModel):
    username: str
    password: str
