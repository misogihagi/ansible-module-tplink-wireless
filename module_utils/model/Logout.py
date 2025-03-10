from pydantic import BaseModel


class Logout(BaseModel):
    confirmed: bool
