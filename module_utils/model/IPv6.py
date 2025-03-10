from pydantic import BaseModel


class IPv6(BaseModel):
    ipv6_status: str
    ipv6_wan: str
    ipv6_lan: str
