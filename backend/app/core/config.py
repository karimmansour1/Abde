from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "JNRCS CRM API"
    api_prefix: str = "/api/v1"
    database_url: str = "sqlite:///./jnrcs_crm.db"

    # Supabase (optional when using Postgres on Supabase)
    supabase_url: str | None = None
    supabase_anon_key: str | None = None
    supabase_service_role_key: str | None = None

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
