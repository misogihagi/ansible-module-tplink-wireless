from pydantic import BaseModel


class Security(BaseModel):
    basic_security: str
    advanced_security: str
    local_management: bool
    remote_management: bool
