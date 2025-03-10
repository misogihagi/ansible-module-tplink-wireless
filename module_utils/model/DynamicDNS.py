from pydantic import BaseModel


class DynamicDNS(BaseModel):
    enabled: bool
