from pydantic_settings import BaseSettings
from typing import Optional
import secrets


class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://user:password@localhost/app_db"
    SECRET_KEY: str = secrets.token_hex(32)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"


settings = Settings()