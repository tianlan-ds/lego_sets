from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class Browser(object):
    _WINDOW_SIZE = "1920,1080"

    _chrome_options = Options()
    _chrome_options.add_argument("--headless")
    _chrome_options.add_argument("--window-size=%s" % _WINDOW_SIZE)

    _chrome_path = '/usr/local/bin/chromedriver'

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=self._chrome_path, chrome_options=self._chrome_options)

    def get(self, url: str):
        self.driver.get(url)

    def find_elements_by_class_name(self, class_name: str):
        return self.driver.find_element_by_class_name(class_name)

    def tear_down(self, seconds: int = 3):
        time.sleep(seconds)
        self.driver.stop_client()
        self.driver.close()

    @property
    def page_source(self):
        return self.driver.page_source
