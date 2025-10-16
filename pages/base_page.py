from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 12

class BasePage:
    def __init__(self, driver, timeout=DEFAULT_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, by, locator):
        el = self.wait.until(EC.element_to_be_clickable((by, locator)))
        el.click()
        return el

    def type(self, text, by, locator, clear=True):
        el = self.wait.until(EC.presence_of_element_located((by, locator)))
        if clear:
            el.clear()
        el.send_keys(text)
        return el

    def present(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def visibles(self, by, locator):
        return self.wait.until(EC.presence_of_all_elements_located((by, locator)))

    def visible(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator)))
