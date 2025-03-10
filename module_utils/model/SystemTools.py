from typing import TypedDict
from playwright.sync_api import Page
from pydantic import BaseModel
from ._base import TPLinkBaseModel


class User(TypedDict):
    username: str
    password: str


class PasswordChange(BaseModel):
    username: str
    password: str

    def run(self, page: Page, username: str, password: str):
        page.locator("#frame1").content_frame.get_by_role(
            "link", name="システム ツール"
        ).click()
        page.locator("#frame1").content_frame.get_by_role(
            "link", name="- パスワード"
        ).click()
        page.locator("#frame2").content_frame.locator("#curName").click()
        page.locator("#frame2").content_frame.locator("#curName").fill(username)
        page.locator("#frame2").content_frame.locator("#curName").press("Tab")
        page.locator("#frame2").content_frame.locator("#curPwd").fill(password)
        page.locator("#frame2").content_frame.locator("#curPwd").press("Tab")
        page.locator("#frame2").content_frame.locator("#newName").fill(self.username)
        page.locator("#frame2").content_frame.locator("#newName").press("Tab")
        page.locator("#frame2").content_frame.locator("#newPwd").fill(self.password)
        page.locator("#frame2").content_frame.locator("#newPwd").press("Tab")
        page.locator("#frame2").content_frame.locator("#cfmPwd").fill(self.password)
        page.locator("#frame2").content_frame.get_by_role("button", name="保存").click()
        page.get_by_role("textbox", name="ユーザー名かパスワードが違います").click()
        page.get_by_role("textbox", name="ユーザー名かパスワードが違います").fill(
            self.username
        )
        page.get_by_role("textbox", name="ユーザー名かパスワードが違います").press(
            "Tab"
        )
        page.get_by_role("textbox", name="パスワード", exact=True).fill(self.password)
        page.get_by_role("textbox", name="パスワード", exact=True).press("Enter")


class SystemTools(TPLinkBaseModel):
    time_settings: str
    diagnostics: str
    firmware_upgrade: str
    factory_reset: bool
    backup_restore: str
    restart: bool
    password_change: PasswordChange
    system_log: str
    statistics: str

    def run(self, page: Page, username: str, password: str):
        self.password_change.run(page, username=username, password=password)
