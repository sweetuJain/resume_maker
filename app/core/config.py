from pydantic_settings import BaseSettings
from functools import lru_cache
import os


class Settings(BaseSettings):
    ENV: str
    DEBUG: bool
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    JWT_SECRET: str
    JWT_ALGO: str
    JWT_EXPIRE_MIN: int 

    class Config:
        env_file = f".env.{os.getenv('ENV', 'local')}"
        case_sensitive = True

# @lru_cache()
    #LRU - Least Recently Used, cache the settings instance - improves performance - only one instance is created - avoids re-reading env file multiple times - thread-safe - suitable for web applications - reduces latency - memory efficient - avoids redundant computations - improves scalability - enhances user experience - simplifies code maintenance - promotes best practices
    # Ye Python ka built-in decorator hai
    # Function ko wrap karta hai
    # Function ke input → output ka map memory me rakhta hai
@lru_cache()
def get_settings() -> Settings:
    return Settings()


 # env configuration