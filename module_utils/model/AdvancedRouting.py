from typing import List
from pydantic import BaseModel


class AdvancedRouting(BaseModel):
    static_route_list: List[str]
    system_route_table: List[str]
