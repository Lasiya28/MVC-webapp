from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from typing import Optional
import secrets
import os

load_dotenv(dotenv_path="app/.env")

db_username = os.getenv("DATABASE_USERNAME")
db_password = os.getenv("DATABASE_PASSWORD")

# Check if the environment variables are loaded correctly
if not db_username or not db_password:
    raise ValueError("DATABASE_USERNAME or DATABASE_PASSWORD not found in .env file")

class Settings(BaseSettings):
    DATABASE_URL: str = f"mysql+pymysql://{db_username}:{db_password}@localhost/mvc_db"
    SECRET_KEY: str = secrets.token_hex(32)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
