from typing import Optional
from pydantic import BaseModel
from playwright.sync_api import Page


class LAN(
    BaseModel
):  # todo: https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.IPvAnyAddress
    ip_address: str
    subnet_mask: str

    @classmethod
    def run(cls, page: Page):
        page.locator("#frame1").content_frame.get_by_role(
            "link", name="ネットワーク", exact=True
        ).click()
        page.locator("#frame1").content_frame.get_by_role("link", name="- LAN").click()
        page.locator("#frame2").content_frame.locator("#lanIp").click()
        page.locator("#frame2").content_frame.locator("#lanIp").fill(cls.ip_address)
        page.locator("#frame2").content_frame.locator("#lanIp").press("Tab")
        page.locator("#frame2").content_frame.locator("#netmask").press("ArrowRight")
        page.locator("#frame2").content_frame.locator("#netmask").fill(cls.subnet_mask)
        page.locator("#frame2").content_frame.get_by_role("button", name="保存").click()


class Network(BaseModel):
    WAN: str
    LAN: LAN
    mac_clone: Optional[str]

    @classmethod
    def run(cls, page: Page):
        LAN.run(page, cls.LAN)
