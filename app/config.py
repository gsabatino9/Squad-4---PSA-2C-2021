from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    database_url: str = ""
    clients_url: str = ""
    tickets_url: str = ""
    employee_url: str = ""

    class Config:
        env_file = ".env.test" if 'ENV' in os.environ and os.environ['ENV'] == 'TEST' else  ".env"


settings = Settings()