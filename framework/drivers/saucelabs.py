from selenium import webdriver

from framework.util import configuration

SAUCELABS_HUB_URL = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"

SAUCELABS_USERNAME = configuration.saucelabs_username()
SAUCELABS_KEY = configuration.saucelabs_key()
SAUCELABS_TUNNEL_NAME = configuration.saucelabs_tunnel_name()


def get():
    sauce_url = SAUCELABS_HUB_URL % (SAUCELABS_USERNAME, SAUCELABS_KEY)

    caps = {'browserName': "chrome",
            'platform': "Windows 10",
            'version': "54.0",
            'tunnel-identifier': SAUCELABS_TUNNEL_NAME,
            'name': "Minitest Automation"}

    driver = webdriver.Remote(
        desired_capabilities=caps,
        command_executor=sauce_url
    )

    driver.maximize_window()
    return driver
