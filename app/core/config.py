from enum import Enum
from functools import lru_cache

from pydantic import Field, HttpUrl, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppEnv(str, Enum):
    development = "development"
    staging = "staging"
    production = "production"
    test = "test"


class Settings(BaseSettings):
    app_name: str = "Personal Phone Agent"
    app_env: AppEnv = AppEnv.development
    app_debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000

    public_base_url: HttpUrl = "https://example.com"

    openai_api_key: SecretStr = SecretStr("sk-placeholder")
    openai_realtime_model: str = Field(default="gpt-4o-realtime-preview", min_length=1)

    twilio_account_sid: str = Field(default="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", min_length=1)
    twilio_auth_token: SecretStr = SecretStr("twilio-placeholder-token")
    twilio_phone_number: str = "+15551234567"
    owner_phone_number: str = "+15557654321"

    database_url: SecretStr = SecretStr("postgresql://user:password@localhost:5432/personal_phone_agent")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @field_validator("twilio_phone_number", "owner_phone_number")
    @classmethod
    def validate_e164_number(cls, value: str) -> str:
        if not value.startswith("+") or not value[1:].isdigit() or len(value) < 8:
            raise ValueError("must be a valid E.164-style phone number")
        return value


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
