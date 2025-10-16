from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Header(BasePage):
    SEARCH_INPUT  = (By.ID, 'search')
    SEARCH_SUBMIT = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON     = (By.CSS_SELECTOR, '[data-test="@web/CartLink"], [data-test="@web/CartIcon"]')

    def search(self, term):
        self.type(term, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_SUBMIT)

    def open_cart(self):
        self.click(*self.CART_ICON)
