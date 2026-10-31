from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    GROQ_API_KEY: str

    File_MAX_Upload_Size_MB: int
    File_ALLOWED_TYPES: []
    File_Upload_Chunksize: int

    model_config = SettingsConfigDict(
        env_file= '.env'
    )


def get_settings():
    return Settings()