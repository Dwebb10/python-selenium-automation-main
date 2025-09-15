from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By

# ====== Locators ======
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
EMPTY_MESSAGE = (By.XPATH, "//*[contains(text(), 'Your cart is empty')]")

SEARCH_BOX = (By.CSS_SELECTOR, "input[data-test='@web/Search/SearchInput']")
SEARCH_SUBMIT = (By.CSS_SELECTOR, "button[data-test='@web/Search/SearchButton']")
PRODUCT_TILES = (By.CSS_SELECTOR, "[data-test='product-title']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[data-test='shippingButton']")
VIEW_CART_BTN = (By.XPATH, "//a[contains(text(), 'View cart')]")
CART_ITEMS = (By.CSS_SELECTOR, "[data-test='@web/CartLinkQuantity']")

# ====== Steps ======

@given('Open Target homepage')
def open_homepage(context):
    context.driver.get("https://www.target.com/")

@when('I click the cart icon')
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()

@then('Verify that "Your cart is empty" message is shown')
def verify_empty_cart_message(context):
    message = context.driver.find_element(*EMPTY_MESSAGE)
    assert message.is_displayed(), "The empty cart message is NOT displayed."
    sleep(1)


# ---- ADD TO CART TEST ----

@when('I search for "{product}"')
def search_for_product(context, product):
    search_box = context.driver.find_element(*SEARCH_BOX)
    search_box.clear()
    search_box.send_keys(product)
    context.driver.find_element(*SEARCH_SUBMIT).click()

@when('I select the first product from results')
def select_first_product(context):
    context.driver.find_elements(*PRODUCT_TILES)
    products = context.driver.find_elements(*PRODUCT_TILES)
    assert products, "No products found on search results page!"
    products[0].click()



@when('I add the product to the cart')
def add_product_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()



@when('I go to the cart page')
def go_to_cart(context):
    context.driver.find_element(*VIEW_CART_BTN).click()

@then('Verify that the cart has items')
def verify_product_in_cart(context):
    items = context.driver.find_elements(*CART_ITEMS)
    assert len(items) > 0, "Cart appears to be empty — no items or total price found!"
    sleep(3)
