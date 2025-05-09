from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Configurações da API
    API_SETTINGS: dict = {
        "title": "API Vitivinicultura",
        "version": "1.0.0",
        "description": "API para disponibilizar dados públicos da vitivinicultura brasileira, coletados do site da Embrapa."
    }

    DATABASE_URL: str

    # Configurações de segurança
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()