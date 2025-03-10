from typing import Literal, Union
from pydantic import BaseModel

OperatingMode = Union[
    Literal["wireless_router"],
    Literal["wisp"],
    Literal["bridge_mode"],
    Literal["repeater"],
]
