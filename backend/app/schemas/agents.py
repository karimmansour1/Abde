from pydantic import BaseModel


class HumanitarianAgent(BaseModel):
    key: str
    name: str
    purpose: str
    trigger: str
