from playwright.sync_api import Page
from pydantic import BaseModel
from ._base import TPLinkBaseModel
from .Status import Status
from .QuickSetup import QuickSetup
from .OperatingMode import OperatingMode
from .Network import Network
from .Wireless2_4GHz import Wireless2_4GHz
from .GuestNetwork import GuestNetwork
from .DHCP import DHCP
from .Forwarding import Forwarding
from .Security import Security
from .ParentalControl import ParentalControl
from .AccessControl import AccessControl
from .AdvancedRouting import AdvancedRouting
from .BandwidthControl import BandwidthControl
from .IpMacBinding import IpMacBinding
from .DynamicDNS import DynamicDNS
from .IPv6 import IPv6
from .SystemTools import SystemTools
from .Logout import Logout


class RouterConfig(TPLinkBaseModel):
    status: Status
    quick_setup: QuickSetup
    operating_mode: OperatingMode
    network: Network
    wireless_2_4GHz: Wireless2_4GHz
    guest_network: GuestNetwork
    dhcp: DHCP
    forwarding: Forwarding
    security: Security
    parental_control: ParentalControl
    access_control: AccessControl
    advanced_routing: AdvancedRouting
    bandwidth_control: BandwidthControl
    ip_mac_binding: IpMacBinding
    dynamic_dns: DynamicDNS
    ipv6: IPv6
    system_tools: SystemTools
    logout: Logout

    def run(self, page: Page, username: str, password: str):
        self.wireless_2_4GHz.run(page)
        self.system_tools.run(page, username=username, password=password)
