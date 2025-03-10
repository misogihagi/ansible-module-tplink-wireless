from pydantic import BaseModel


class QuickSetup(BaseModel):
    setup_type: str
