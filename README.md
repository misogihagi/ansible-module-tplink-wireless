# ansible-module-tplink-wireless
  Ansible modules for TP Link wireless router

This repository provides a custom Ansible module that automates GUI configurations using Playwright. The module can be used to log into web applications as part of an Ansible automation workflow.

## TODO

- [] ステータス
- [] クイック セットアップ
- [] 動作するモード
- [] ネットワーク
  - [] WAN
  - [] LAN
  - [] MAC クローン
- [] ワイヤレス 2.4GHz
  - [] 基本設定
  - [] WPS
  - [] ワイヤレス セキュリティ
  - [] ワイヤレス MAC フィルタリング
  - [] ワイヤレス詳細設定
  - [] ワイヤレス統計
- [] ゲスト ネットワーク
- [] DHCP
  - [] DHCP 設定
  - [] DHCP クライアント リスト
  - [] アドレス予約
- [] 転送
  - [] 仮想 サーバー
  - [] ポート トリガー
  - [] DMZ
  - [] UPnP
- [] セキュリティ
  - [] 基本セキュリティ
  - [] 高度セキュリティ
  - [] ローカル管理
  - [] リモート管理
- [] 保護者による制限
- [] アクセス制御
  - [] ルール
  - [] ホスト
  - [] ターゲット
  - [] スケジュール
- [] 高度経路
  - [] 静的経路リスト
  - [] システム経路テーブル
- [] 帯域幅制御
- [] IP & MAC バインディング
  - [] バインディング 設定
  - [] ARP リスト
- [] 動的 DNS
- [] IPv6
  - [] IPv6 ステータス
  - [] IPv6 WAN
  - [] IPv6 LAN
- [] システム ツール
  - [] 時刻設定
  - [] 診断
  - [] ファームウェア アップグレード
  - [] 工場出荷時の設定
  - [] バックアップ & 復元
  - [] 再起動
  - [] パスワード
  - [] システム ログ
  - [] 統計
- [] ログアウト


## Prerequisites

Before using this module, ensure that you have the following dependencies installed:

### Install Python and Required Packages
```bash
pip install ansible playwright
playwright install
```

If using Docker or a minimal system, install Playwright dependencies:
```bash
playwright install --with-deps
```

## Module Description

This module launches a browser (headless by default), navigates to the login page, enters user credentials, and verifies the login by retrieving the page title.

## Module File Structure
```
ansible/
│── modules/
│   ├── playwright_login.py
│── playbook.yml
│── README.md
```

## Module Usage

### 1. Place the module in the appropriate Ansible directory
Copy `playwright_login.py` to the `library/` directory inside your Ansible project.

### 2. Example Playbook
Create a playbook (`playbook.yml`) to use the module:
```yaml
- hosts: localhost
  tasks:
    - name: Log into the web application
      playwright_login:
        url: "https://example.com/login"
        username: "your_username"
        password: "your_password"
      register: login_result

    - debug:
        var: login_result.title
```

### 3. Run the Playbook
Execute the playbook using Ansible:
```bash
ansible-playbook playbook.yml
```

```bash
. .venv/bin/activate
python -m ansible playbook demo.yml
```

## Module Parameters

| Parameter  | Required | Description |
|------------|----------|------------------------------------------------|
| `url`      | Yes      | The login page URL |
| `username` | Yes      | The username for login |
| `password` | Yes      | The password for login (hidden in logs) |

## Features
- Supports Chromium-based browsers
- Runs in headless mode by default
- Logs in and retrieves the page title
- Can be integrated into automation workflows

## Notes
- To debug, set `headless=False` in `playwright_login.py` to view the browser actions.
- Ensure that Playwright browsers are installed using `playwright install`.
- Use `page.screenshot(path="screenshot.png")` in `playwright_login.py` to capture login results.

## License
MIT License

---
This module helps automate web logins with Ansible and Playwright. Contributions and improvements are welcome! 🚀


