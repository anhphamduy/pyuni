import os
import platform

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Client(webdriver.Chrome):
    delay = 10

    def __init__(self, executable_path=None, options=None, headless=True, *args, **kwargs):
        # find the browser driver
        if not executable_path:
            system = platform.system()
            if system == 'Windows':
                os_path = 'windows'
            elif system == 'Darwin':
                os_path = 'darwin'
            else:
                os_path = 'linux'

            executable_path = os.path.join(os.path.dirname(__file__), 'drivers', os_path, 'chromedriver')

        if not options:
            options = Options()

            if headless:
                options.add_argument("--headless")

            options.add_argument("--window-size=%s" % "1920, 1080")

        super().__init__(executable_path=executable_path, options=options, *args, **kwargs)

    def find_element_by_css_selector(self, css_selector):
        WebDriverWait(self, self.delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        return self.find_element(by=By.CSS_SELECTOR, value=css_selector)
