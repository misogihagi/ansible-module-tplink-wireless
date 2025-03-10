from typing import List
from pydantic import BaseModel


class DHCP(BaseModel):
    dhcp_settings: str
    dhcp_client_list: List[str]
    address_reservation: List[str]
