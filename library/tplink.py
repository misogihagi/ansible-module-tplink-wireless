from playwright.sync_api import Playwright, sync_playwright, expect, Page
from ansible.module_utils.basic import AnsibleModule

try:
    from ansible.module_utils.RouterConfig import RouterConfig
except ImportError:
    from module_utils.RouterConfig import RouterConfig



def login(page, url, username, password):
      page.goto(url)
      page.get_by_placeholder("ユーザー名かパスワードが違います").click()
      page.get_by_placeholder("ユーザー名かパスワードが違います").fill(username)
      page.get_by_placeholder("ユーザー名かパスワードが違います").press("Tab")
      page.get_by_placeholder("パスワード", exact=True).fill(password)
      page.get_by_placeholder("パスワード", exact=True).press("Enter")
      expect(page.locator("frame[name=\"topFrame\"]")).to_be_visible()
      return page


def run(url, username, password, configuration):
     with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      context = browser.new_context()
      page = context.new_page()
      config = RouterConfig(**configuration)
      print(config)
      page = login(page, url, username, password)
      context.close()
      browser.close()
 

def main():
    module_args = dict(
        url=dict(type='str', required=True),
        username=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        configuration=dict(type='dict', required=True),
    )


    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    url = module.params['url']
    username = module.params['username']
    password = module.params['password']
    configuration = module.params['configuration']

    try:
      run(url, username, password, configuration)
      module.exit_json(changed=False)

    except Exception as e:
        module.fail_json(msg=str(e))

if __name__ == '__main__':
    main()

