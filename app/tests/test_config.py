import pytest
from pydantic import ValidationError

from app.core.config import AppEnv, Settings


@pytest.fixture
def required_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("PUBLIC_BASE_URL", "https://example.com")
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test-key")
    monkeypatch.setenv("OPENAI_REALTIME_MODEL", "gpt-4o-realtime-preview")
    monkeypatch.setenv("TWILIO_ACCOUNT_SID", "AC1234567890")
    monkeypatch.setenv("TWILIO_AUTH_TOKEN", "auth-token")
    monkeypatch.setenv("TWILIO_PHONE_NUMBER", "+15551234567")
    monkeypatch.setenv("OWNER_PHONE_NUMBER", "+15557654321")
    monkeypatch.setenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/db")


def test_settings_load_from_environment(monkeypatch: pytest.MonkeyPatch, required_env: None) -> None:
    monkeypatch.setenv("APP_ENV", "production")

    settings = Settings()

    assert settings.app_env == AppEnv.production
    assert str(settings.public_base_url) == "https://example.com/"
    assert settings.openai_api_key.get_secret_value() == "sk-test-key"


def test_settings_redacts_secrets_in_repr(required_env: None) -> None:
    settings = Settings()

    rendered = repr(settings)

    assert "sk-test-key" not in rendered
    assert "auth-token" not in rendered
    assert "postgresql://user:pass@localhost:5432/db" not in rendered


def test_settings_validates_phone_number(monkeypatch: pytest.MonkeyPatch, required_env: None) -> None:
    monkeypatch.setenv("OWNER_PHONE_NUMBER", "5557654321")

    with pytest.raises(ValidationError):
        Settings()
