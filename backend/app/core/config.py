"""_Creates configuration settings from environment variables_
"""

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True, extra="ignore")

    PROJECT_NAME:str

    JWT_KEY:str
    JWT_ALGORITHM:str
    JWT_EXPIRY_MINUTES:int

    DB_URL:str

    ORIGINS:list[str]

    
settings = Settings()