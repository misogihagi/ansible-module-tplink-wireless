from typing import List
from pydantic import BaseModel


class ParentalControl(BaseModel):
    restrictions: List[str]
