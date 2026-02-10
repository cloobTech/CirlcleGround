from datetime import timedelta, datetime, timezone
from src.core.pydantic_confirguration import config
from jose import jwt, JWTError


def create_access_token(data: dict, expires_delta: int = 5800):
    to_encode = data.copy()
    expire = datetime.now(
        timezone.utc) + (timedelta(minutes=expires_delta or config.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str, credential_exceptions: Exception):
    try:
        payload = jwt.decode(token, config.SECRET_KEY,
                             algorithms=config.ALGORITHM)

        return payload
    except JWTError as exc:
        raise credential_exceptions from exc


def retrieve_token(user):
    payload = {
        "sub": str(user.id),
        "role": user.role
    }

    access_token = create_access_token(payload)
    return access_token
