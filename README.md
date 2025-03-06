# ansible-module-tplink-wireless
  Ansible modules for TP Link wireless router

This repository provides a custom Ansible module that automates GUI configurations using Playwright. The module can be used to log into web applications as part of an Ansible automation workflow.

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


