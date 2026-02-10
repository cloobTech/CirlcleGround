from pydantic_settings import BaseSettings, SettingsConfigDict


class PydanticConfiguration(BaseSettings):

    SECRET_KEY: str = "secret"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    MAIL_FROM: str = "4Eo9f@example.com"
    MAIL_PASSWORD: str = "password"
    DEV_ENV: str = 'development'

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8")


config = PydanticConfiguration()
