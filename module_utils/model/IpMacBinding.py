from typing import List
from pydantic import BaseModel


class IpMacBinding(BaseModel):
    binding_settings: str
    arp_list: List[str]
