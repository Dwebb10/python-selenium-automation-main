from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC

def w(ctx, t=12): return W(ctx.driver, t)

@given('Open Target homepage')
def open_home(ctx):
    ctx.driver.get("https://www.target.com/")

@when('I click the cart icon')
def click_cart_icon(ctx):
    CART = (By.CSS_SELECTOR, '[data-test="@web/CartLink"], [data-test="@web/CartIcon"]')
    w(ctx).until(EC.element_to_be_clickable(CART)).click()

@then('Verify that "Your cart is empty" message is shown')
def verify_empty_cart_message(ctx):
    EMPTY = (By.XPATH, "//*[contains(text(),'Your cart is empty')]")
    assert w(ctx).until(EC.visibility_of_element_located(EMPTY))

# ----- add-to-cart flow -----

@when('I select the first product from results')
def select_first_product(ctx):
    TITLES = (By.CSS_SELECTOR, '[data-test="product-title"] a, [data-test="product-title"]')
    w(ctx).until(EC.presence_of_all_elements_located(TITLES))
    tiles = [t for t in ctx.driver.find_elements(*TITLES) if t.is_displayed()]
    assert tiles, "No visible products found in search results."
    tiles[0].click()

@when('I add the product to the cart')
def add_to_cart(ctx):
    ADD = (By.CSS_SELECTOR, 'button[data-test="shippingButton"], button[data-test="addToCartButton"]')
    w(ctx).until(EC.element_to_be_clickable(ADD)).click()

@when('I go to the cart page')
def go_to_cart(ctx):
    VIEW_CART = (By.XPATH, "//a[contains(., 'View cart')] | //button[contains(., 'View cart')]")
    w(ctx).until(EC.element_to_be_clickable(VIEW_CART)).click()

@then('Verify that the cart has items')
def verify_cart_has_items(ctx):
    QTY_BADGE = (By.CSS_SELECTOR, '[data-test="@web/CartLinkQuantity"]')
    LINE_ITEM = (By.CSS_SELECTOR, '[data-test="cartItem"], [data-test="lineItem"]')
    try:
        qty_el = w(ctx, 10).until(EC.visibility_of_element_located(QTY_BADGE))
        assert int(qty_el.text.strip()) >= 1
    except Exception:
        items = ctx.driver.find_elements(*LINE_ITEM)
        assert len(items) >= 1, "Cart appears to be empty."



