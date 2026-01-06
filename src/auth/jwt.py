from datetime import timedelta, datetime, timezone
from src.core.pydanctic_confirguration import config
from jose import jwt, JWTError


async def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=[config.ALGORITHM])
    return encoded_jwt  
    # except Exception as e:
    #     return{"status": "failed",
    #            "message": "Error generating jwt"}


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=config.ALGORITHM)
        user_id: str = payload.get("sub")
        if user_id is None:
            return None
        return user_id 
    except JWTError:
        return None
    

def retrieve_token(user):
    payload = {
        "user_id": user.id,
        "user_role": user.role
    }
    access_token = create_access_token(payload)
    return access_token