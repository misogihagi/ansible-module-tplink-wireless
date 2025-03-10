from typing import List
from pydantic import BaseModel


class Forwarding(BaseModel):
    virtual_server: List[str]
    port_trigger: List[str]
    dmz: bool
    upnp: bool
