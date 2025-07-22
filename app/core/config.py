from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = "sqlite:///./database.db"
    TRON_NETWORK: str = "shasta"

settings = Settings()