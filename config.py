from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvVariables(BaseSettings):
    WA_SESSION_ID: str
    WA_API_URL: str
    WA_API_KEY: str

    RECEPIENT_NUMBER: str

    model_config = SettingsConfigDict(env_file=".env")


env = EnvVariables()
