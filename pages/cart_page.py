from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    EMPTY_MESSAGE = (By.XPATH, "//*[contains(text(), 'Your cart is empty')]")

    def empty_message_is_visible(self):
        self.visible(*self.EMPTY_MESSAGE)
        return True
