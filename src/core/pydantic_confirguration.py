from pydantic_settings import BaseSettings, SettingsConfigDict


class PydanticConfiguration(BaseSettings):

    SECRET_KEY: str = "secret"
    ALGORITHM: str = "HS256"
    REDIS_URL: str = "redis://localhost:6379"
    RESEND_API_KEY: str = ""
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    MAIL_FROM: str = "4Eo9f@example.com"
    MAIL_PASSWORD: str = "password"
    DEV_ENV: str = 'development'
    DATABASE_URL: str = ""


    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8")


config = PydanticConfiguration()
