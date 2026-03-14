from fastapi import FastAPI

from app.api.agents import router as agents_router
from app.api.beneficiaries import router as beneficiaries_router
from app.api.cases import router as cases_router
from app.api.integrations import router as integrations_router
from app.api.volunteers import router as volunteers_router
from app.api.workflows import router as workflows_router
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine

app = FastAPI(title=settings.app_name)


@app.on_event("startup")
def startup() -> None:
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "JNRCS CRM API online"}


app.include_router(beneficiaries_router, prefix=settings.api_prefix)
app.include_router(volunteers_router, prefix=settings.api_prefix)
app.include_router(cases_router, prefix=settings.api_prefix)
app.include_router(workflows_router, prefix=settings.api_prefix)
app.include_router(agents_router, prefix=settings.api_prefix)
app.include_router(integrations_router, prefix=settings.api_prefix)
