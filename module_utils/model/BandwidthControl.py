from pydantic import BaseModel


class BandwidthControl(BaseModel):
    bandwidth_limit: int
