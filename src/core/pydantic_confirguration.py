from pydantic_settings import BaseSettings, SettingsConfigDict

class PydanticConfiguration(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = "60"
    MAIL_FROM: str 
    MAIL_PASSWORD: str
    


config = PydanticConfiguration()