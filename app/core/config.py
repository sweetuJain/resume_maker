from pydentic import BaseSettings

class Settings(BaseSettings):
    ENV: str
    DB_URL: str
    API_KEY: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    JWT_EXPIRATION_MINUTES: int
    
settings = Settings()

 # env configuration