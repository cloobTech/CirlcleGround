from pydantic import BaseModel, EmailStr, model_validator, ConfigDict
from typing import Literal
import phonenumbers
from src.core.exceptions import InvalidCredentialsError
from phonenumbers.phonenumberutil import NumberParseException


class BaseUser(BaseModel):
    email: EmailStr


class CreateUserSchema(BaseUser):
    first_name: str
    last_name: str
    phone_number: str
    password: str
    confirm_password: str
    location: str
    

    
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


class LoginUser(BaseModel):
    username: str
    password: str


class ReadUser(BaseUser):
    model_config = ConfigDict(from_attributes=True)

    first_name: str
    last_name: str
    phone_number: str
    location: str
    role: str


class UpdateUser(BaseUser):
    first_name: str
    last_name: str
    phone_number: str
    location: str
    role: str 