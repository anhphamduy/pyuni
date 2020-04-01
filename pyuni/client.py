import os
import platform

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Client(webdriver.Chrome):
    def __init__(self, university, executable_path=None, options=None, headless=True, *args, **kwargs):
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

        self.university = university
        self.is_authenticated = False

    def authenticate(self, username, password):
        raise NotImplementedError()
