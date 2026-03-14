from fastapi import APIRouter

from app.schemas.agents import HumanitarianAgent
from app.services.agents import AGENTS

router = APIRouter(prefix="/agents", tags=["agents"])


@router.get("", response_model=list[HumanitarianAgent])
def list_agents():
    return AGENTS
