from pydantic_settings import BaseSettings
from pydantic import Field
from functools import lru_cache

class Settings(BaseSettings):
    env: str = Field("development", env="ENV")
    database_url: str = Field("sqlite:///./test.db", env="DATABASE_URL")
    postgres_url: str = Field("postgresql://user:password@localhost:5432/emaildb", env="POSTGRES_URL")

    smtp_host: str = Field("localhost", env="SMTP_HOST")
    smtp_port: int = Field(587, env="SMTP_PORT")
    smtp_username: str = Field("", env="SMTP_USERNAME")
    smtp_password: str = Field("", env="SMTP_PASSWORD")
    email_from: str = Field("noreply@example.com", env="EMAIL_FROM")

    log_level: str = Field("INFO", env="LOG_LEVEL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache()
def get_settings() -> Settings:
    return Settings()
