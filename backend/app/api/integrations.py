from fastapi import APIRouter

from app.integrations.supabase import get_supabase_config

router = APIRouter(prefix="/integrations", tags=["integrations"])


@router.get("/supabase")
def supabase_status():
    return {"provider": "supabase", "config": get_supabase_config()}
