import bcrypt
import hmac
import hashlib
from src.core.pydantic_confirguration import config


def hash(password: str) -> str:
    """ hash password """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """function to verify password"""
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


def verify_signature(payload: bytes, signature: str):
    secret_key = config.PAYSTACK_SECRET_KEY.encode("utf-8")


    hashed_result = hmac.new(
        key=secret_key,
        msg=payload,
        digestmod=hashlib.sha512
    ).hexdigest()

    return hmac.compare_digest(hashed_result, signature)
