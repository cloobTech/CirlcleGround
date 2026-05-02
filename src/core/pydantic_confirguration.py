from pydantic_settings import BaseSettings, SettingsConfigDict


class PydanticConfiguration(BaseSettings):

    SECRET_KEY: str = "secret"
    ALGORITHM: str = "HS256"
    REDIS_URL: str = "redis://localhost:6379"
    PAYSTACK_BASE_URL: str = "https://api.paystack.co"
    PAYSTACK_TEST_MODE: str = "test"
    PAYSTACK_PAYMENT_URL: str = "https://api.paystack.co/transaction/initialize"
    PAYSTACK_TRANSFER_URL: str = "https://api.paystack.co/transfer"
    PAYSTACK_RECIPIENT_URL: str = "https://api.paystack.co/transferrecipient"
    PAYSTACK_BANK_CODES_URL: str = "https://api.paystack.co/bank"
    PAYSTACK_BANK_RESOLVE_URL: str = "https://api.paystack.co/bank/resolve"
    PAYSTACK_VERIFICATION_URL: str = "https://api.paystack.co/transaction/verify"
    RESEND_API_KEY: str = ""
    PAYSTACK_SECRET_KEY: str = "sk_test_375726c9f21e6ef444405c55e2b512a691c38e52"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    MAIL_FROM: str = "4Eo9f@example.com"
    MAIL_PASSWORD: str = "password"
    DEV_ENV: str = 'development'
    DATABASE_URL: str = ""
    UPDATE_WINDOW_MINUTES: int = 60


    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8")


config = PydanticConfiguration()
