# pages/main_page.py
from pages.base_page import BasePage

class MainPage(BasePage):
    URL = "https://www.target.com/"

    def open(self):
        self.driver.get(self.URL)
