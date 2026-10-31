from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    GROQ_API_KEY: str
    MAX_File_Upload_Size_MB: int
    File_ALLOWED_TYPES: []

    model_config = SettingsConfigDict(
        env_file= '.env'
    )


def get_settings():
    return Settings()