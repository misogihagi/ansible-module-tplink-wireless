from pydantic import BaseModel


class GuestNetwork(BaseModel):
    enabled: bool
