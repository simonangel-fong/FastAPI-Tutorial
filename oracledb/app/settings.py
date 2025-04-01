from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ORACLE_DB_HOST: str
    ORACLE_DB_PORT: str
    ORACLE_DB_SERVICE: str
    ORACLE_DB_USER: str
    ORACLE_DB_PWD: str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()
