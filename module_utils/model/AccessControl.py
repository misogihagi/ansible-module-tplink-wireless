from typing import List
from pydantic import BaseModel


class AccessControl(BaseModel):
    rules: List[str]
    hosts: List[str]
    targets: List[str]
    schedule: str
