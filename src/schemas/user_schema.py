from pydantic import BaseModel, EmailStr, model_validator, ConfigDict, Field
import phonenumbers
from src.core.exceptions import InvalidCredentialsError
from phonenumbers.phonenumberutil import NumberParseException
from src.enums.enums import UserRole


class BaseUser(BaseModel):
    email: EmailStr


class CreateUserSchema(BaseUser):
    first_name: str
    last_name: str
    phone_number: str
    password: str
    location: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    role: UserRole = UserRole.GUEST_USER

    @model_validator(mode="before")
    def phone_number_format(cls, values):
        phone_number = values.get("phone_number")
        if phone_number:
            try:
                num = phonenumbers.parse(phone_number, "NG")
                if phonenumbers.is_valid_number(num):
                    values["phone_number"] = phonenumbers.format_number(
                        num, phonenumbers.PhoneNumberFormat.E164)
            except NumberParseException:
                raise InvalidCredentialsError(
                    details={
                        "recommendations": "Phone number could not be parsed"}
                )
        return values


class LoginUser(BaseModel):
    email: EmailStr | None = None
    phone_number: str | None = None
    password: str

    @model_validator(mode="after")
    def validate_identifier(self):
        if not self.email and not self.phone_number:
            raise ValueError("Either email or phone number must be provided")
        return self


class ReadUser(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    location: str
    role: UserRole

    model_config = ConfigDict(from_attributes=True)
