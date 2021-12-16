from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = ""
    clients_url: str = ""
    tickets_url: str = ""
    employee_url: str = ""

    class Config:
        env_file = ".env"


settings = Settings()