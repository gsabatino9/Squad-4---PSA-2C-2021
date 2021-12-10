from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "test"

    class Config:
        env_file = ".env"


settings = Settings()