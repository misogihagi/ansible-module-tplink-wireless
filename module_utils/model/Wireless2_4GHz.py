from typing import Literal, Union, Optional
from pydantic import BaseModel, Field, conlist

from typing import TypedDict
from playwright.sync_api import Page, expect, TimeoutError as PlaywrightTimeoutError
from pydantic import BaseModel
from ._base import TPLinkBaseModel

wireless_basic_settings_mapper = {
    "mode": {
        "11n": "n-only",
        "11gn": "gn",
        "11bgn": "n",
    },
    "channel": {
        "auto": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "10": "10",
        "11": "11",
        "12": "12",
        "13": "13",
    },
    "bandwidth": {
        "auto": "Auto",
        "20MHz": "20M",
        "40MHz": "40M",
    },
}


class WirelessBasicSettings(BaseModel):
    network_name: str
    mode: Union[
        Literal["11n"],
        Literal["11gn"],
        Literal["11bgn"],
    ]
    channel: Union[
        Literal["auto"],
        Literal["1"],
        Literal["2"],
        Literal["3"],
        Literal["4"],
        Literal["5"],
        Literal["6"],
        Literal["7"],
        Literal["8"],
        Literal["9"],
        Literal["10"],
        Literal["11"],
        Literal["12"],
        Literal["13"],
    ]
    bandwidth: Union[
        Literal["auto"],
        Literal["20MHz"],
        Literal["40MHz"],
    ]
    ssid_broadcast_enabled: bool

    def run(self, page: Page):
        page.locator("#frame1").content_frame.get_by_role(
            "link", name="ワイヤレス 2.4GHz"
        ).click()
        page.locator("#frame2").content_frame.locator("#ssid").click()
        page.locator("#frame2").content_frame.locator("#ssid").fill(self.network_name)
        page.locator("#frame2").content_frame.locator("#mode").select_option(
            wireless_basic_settings_mapper["mode"][self.mode]
        )
        page.locator("#frame2").content_frame.locator("#channel").select_option(
            wireless_basic_settings_mapper["channel"][self.channel]
        )
        page.locator("#frame2").content_frame.locator("#bandWidth").select_option(
            wireless_basic_settings_mapper["bandwidth"][self.bandwidth]
        )
        if self.ssid_broadcast_enabled:
            page.locator("#frame2").content_frame.locator("#ssidBroadcast").check()
        else:
            page.locator("#frame2").content_frame.locator("#ssidBroadcast").uncheck()
        page.locator("#frame2").content_frame.get_by_role("button", name="保存").click()
        expect(
            page.locator("#frame2").content_frame.locator('[id="_load"]')
        ).to_be_hidden(timeout=20_000)


def run_wps(page: Page, enable_wps: Optional[bool]):
    print(enable_wps)
    page.locator("#frame1").content_frame.get_by_role(
        "link", name="ワイヤレス 2.4GHz"
    ).click()
    page.locator("#frame1").content_frame.get_by_role("link", name="- WPS").click()

    if enable_wps:
        try:
            if expect(
                page.locator("#frame2").content_frame.get_by_role(
                    "button", name="有効にする"
                )
            ).to_be_visible():
                page.locator("#frame2").content_frame.get_by_role(
                    "button", name="有効にする"
                ).click()
        except PlaywrightTimeoutError:
            pass
        except AssertionError:
            pass
    else:
        try:
            if expect(
                page.locator("#frame2").content_frame.get_by_role("button", name="無効")
            ).to_be_visible():
                page.locator("#frame2").content_frame.get_by_role(
                    "button", name="無効"
                ).click()
        except PlaywrightTimeoutError:
            pass
        except AssertionError:
            pass


class DisableSecurity(BaseModel):
    disable_security: bool


class WPA_WPA2_Personal_Form:
    version: str
    encryption: str
    wireless_password: str
    group_key_update_interval: str

    def __init__(
        self, version, encryption, wireless_password, group_key_update_interval
    ):
        self.version = version
        self.encryption = encryption
        self.wireless_password = wireless_password
        self.group_key_update_interval = group_key_update_interval


class WPA_WPA2_Personal(BaseModel):
    version: Union[
        Literal["auto"],
        Literal["WPA-PSK"],
        Literal["WPA2-PSK"],
    ]
    encryption: Union[
        Literal["auto"],
        Literal["TKIP"],
        Literal["AES"],
    ]
    wireless_password: str
    group_key_update_interval: int

    def to_form(self):
        version_mapper = {
            "auto": "0",
            "WPA-PSK": "1",
            "WPA2-PSK": "2",
        }
        encryption_mapper = {
            "auto": "0",
            "TKIP": "1",
            "AES": "2",
        }
        return WPA_WPA2_Personal_Form(
            version_mapper[self.version],
            encryption_mapper[self.encryption],
            self.wireless_password,
            str(self.group_key_update_interval),
        )


class WPA_WPA2_Enterprise_Form:
    version: str
    encryption: str
    radius_server_ip: str
    radius_server_port: str
    radius_server_password: str
    group_key_update_interval: str

    def __init__(
        self,
        version,
        encryption,
        radius_server_ip,
        radius_server_port,
        radius_server_password,
        group_key_update_interval,
    ):
        self.version = version
        self.encryption = encryption
        self.radius_server_ip = radius_server_ip
        self.radius_server_port = radius_server_port
        self.radius_server_password = radius_server_password
        self.group_key_update_interval = group_key_update_interval


class WPA_WPA2_Enterprise(BaseModel):
    version: Union[
        Literal["auto"],
        Literal["WPA"],
        Literal["WPA2"],
    ]
    encryption: Union[
        Literal["auto"],
        Literal["TKIP"],
        Literal["AES"],
    ]
    radius_server_ip: str
    radius_server_port: int
    radius_server_password: str
    group_key_update_interval: int

    def to_form(self):
        version_mapper = {
            "auto": "0",
            "WPA": "1",
            "WPA2": "2",
        }
        encryption_mapper = {
            "auto": "0",
            "TKIP": "1",
            "AES": "2",
        }
        return WPA_WPA2_Personal_Form(
            version_mapper[self.version],
            encryption_mapper[self.encryption],
            self.radius_server_ip,
            str(self.radius_server_port),
            self.radius_server_password,
            str(self.group_key_update_interval),
        )


class WEP_KEY(BaseModel):
    key: str
    key_type: Union[
        Literal["disable"],
        Literal["64bit"],
        Literal["128bit"],
    ]


class WEP_Form:
    auth_type: str
    wep_key_format: str
    selected_keys: conlist(WEP_KEY, max_length=4)

    def __init__(
        self,
        auth_type,
        wep_key_format,
        selected_keys,
    ):
        self.auth_type = auth_type
        self.wep_key_format = wep_key_format
        self.selected_keys = selected_keys


class WEP(BaseModel):
    auth_type: Union[
        Literal["auto"],
        Literal["open"],
        Literal["shared"],
    ]
    wep_key_format: Union[
        Literal["hex"],
        Literal["ascii"],
    ]
    selected_keys: conlist(WEP_KEY, max_length=4)

    def to_form(self):
        wep_key_format_mapper = {
            "hex": "1",
            "ascii": "2",
        }
        return WPA_WPA2_Personal_Form(
            version_mapper[self.version],
            encryption_mapper[self.encryption],
            self.radius_server_ip,
            self.radius_server_port,
            self.radius_server_password,
            self.group_key_update_interval,
        )


WirelessSecurity = Union[
    DisableSecurity,
    WPA_WPA2_Personal,
    WPA_WPA2_Enterprise,
    WEP,
]


def run_wireless_security(page: Page, wireless_security: WirelessSecurity):
    page.locator("#frame1").content_frame.get_by_role(
        "link", name="ワイヤレス 2.4GHz", exact=True
    ).click()
    page.locator("#frame1").content_frame.get_by_role(
        "link", name="- ワイヤレス セキュリティ"
    ).click()

    if isinstance(wireless_security, DisableSecurity):
        page.locator("#frame2").content_frame.locator("#secNone").check()
    if isinstance(wireless_security, WPA_WPA2_Personal):
        form = wireless_security.to_form()
        page.locator("#frame2").content_frame.locator("#secPSK").check()
        page.locator("#frame2").content_frame.locator("#pskAuthType").select_option(
            form.version
        )
        page.locator("#frame2").content_frame.locator("#pskCipher").select_option(
            form.encryption
        )
        page.locator("#frame2").content_frame.locator("#pskSecret").click()
        page.locator("#frame2").content_frame.locator("#pskSecret").fill(
            form.wireless_password
        )
        page.locator("#frame2").content_frame.locator("#pskSecret").press("Tab")
        page.locator("#frame2").content_frame.locator("#interval").fill(
            form.group_key_update_interval
        )
    if isinstance(wireless_security, WPA_WPA2_Enterprise):
        form = wireless_security.to_form()
        page.locator("#frame2").content_frame.locator("#secWPA").check()
        page.locator("#frame2").content_frame.locator("#wpaAuthType").select_option(
            form.version
        )
        page.locator("#frame2").content_frame.locator("#wpaCipher").select_option(
            form.encryption
        )
        page.locator("#frame2").content_frame.get_by_role("paragraph").filter(
            has_text="RADIUS サーバー IP:"
        ).get_by_role("textbox").click()
        page.locator("#frame2").content_frame.get_by_role("paragraph").filter(
            has_text="RADIUS サーバー IP:"
        ).get_by_role("textbox").fill(
            form.radius_server_ip,
        )
        page.locator("#frame2").content_frame.get_by_role("paragraph").filter(
            has_text="RADIUS サーバー IP:"
        ).get_by_role("textbox").press("Tab")
        page.locator("#frame2").content_frame.locator("#wpaSerPort").fill(
            form.radius_server_port
        )
        page.locator("#frame2").content_frame.locator("#wpaSerPort").press("Tab")
        page.locator("#frame2").content_frame.locator("#wpaSerPwd").fill(
            form.radius_server_password
        )
        page.locator("#frame2").content_frame.locator("#wpaSerPwd").press("Tab")
        page.locator("#frame2").content_frame.locator("#wpainterval").fill(
            form.group_key_update_interval
        )
    if isinstance(wireless_security, WEP):
        form = wireless_security.to_form()
        page.locator("#frame2").content_frame.locator("#secWEP").check()
        page.locator("#frame2").content_frame.locator("#wepAuthType").select_option(
            form.auth_type
        )
        page.locator("#frame2").content_frame.locator("#wepKeyType").select_option(
            form.wep_key_format
        )

        def to_form(key_type: str):
            if key_type == "64bit":
                return "40"
            elif key_type == "128bit":
                return "104"
            else:
                return "0"

        if form.selected_keys[0].key_type != "disable":
            page.locator("#frame2").content_frame.locator("#length1").select_option(
                to_form(form.selected_keys[0].key_type)
            )
            page.locator("#frame2").content_frame.get_by_role("paragraph").filter(
                has_text="キー 1: 無効64bit128bit"
            ).get_by_role("textbox").click()
            page.locator("#frame2").content_frame.get_by_role("paragraph").filter(
                has_text="キー 1: 無効64bit128bit"
            ).get_by_role("textbox").fill(form.selected_keys[0].key)

        page.locator("#frame2").content_frame.locator("#length2").select_option(
            to_form(form.selected_keys[1].key_type)
        )
        page.locator("#frame2").content_frame.get_by_role("paragraph").filter(
            has_text="キー 2: 無効64bit128bit"
        ).get_by_role("textbox").click()
        page.locator("#frame2").content_frame.get_by_role("paragraph").filter(
            has_text="キー 2: 無効64bit128bit"
        ).get_by_role("textbox").fill(form.selected_keys[1].key)

        page.locator("#frame2").content_frame.locator("#length3").select_option(
            to_form(form.selected_keys[2].key_type)
        )
        page.locator("#frame2").content_frame.get_by_role("paragraph").filter(
            has_text="キー 3: 無効64bit128bit"
        ).get_by_role("textbox").click()
        page.locator("#frame2").content_frame.get_by_role("paragraph").filter(
            has_text="キー 3: 無効64bit128bit"
        ).get_by_role("textbox").fill(form.selected_keys[2].key)

        page.locator("#frame2").content_frame.locator("#length4").select_option(
            to_form(form.selected_keys[3].key_type)
        )
        page.locator("#frame2").content_frame.get_by_role("paragraph").filter(
            has_text="キー 4: 無効64bit128bit"
        ).get_by_role("textbox").click()
        page.locator("#frame2").content_frame.get_by_role("paragraph").filter(
            has_text="キー 4: 無効64bit128bit"
        ).get_by_role("textbox").fill(form.selected_keys[3].key)

    page.locator("#frame2").content_frame.get_by_role("button", name="保存").click()
    expect(page.locator("#frame2").content_frame.locator('[id="_load"]')).to_be_hidden(
        timeout=20_000
    )


class Wireless2_4GHz(TPLinkBaseModel):
    basic_settings: WirelessBasicSettings
    wps: bool
    wireless_security: WirelessSecurity
    wireless_mac_filtering: bool
    wireless_advanced_settings: str
    wireless_statistics: str

    def run(self, page: Page):
        if self.basic_settings is not None:
            self.basic_settings.run(page)
        if self.wps is not None:
            run_wps(page, self.wps)
        if self.wireless_security is not None:
            run_wireless_security(page, self.wireless_security)
