from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        hide_input_in_errors=True,
    )

    greeting: str = "Добро пожаловать в гостевую книгу!"
    database_url: str


settings = Settings()