from app.core.config import settings


def get_supabase_config() -> dict[str, str | None]:
    return {
        "supabase_url": settings.supabase_url,
        "supabase_anon_key": settings.supabase_anon_key,
        "supabase_service_role_key_set": "yes" if settings.supabase_service_role_key else "no",
        "database_url": settings.database_url,
    }
