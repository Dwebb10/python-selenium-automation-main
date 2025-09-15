from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')
HEADER_LINKS = (By.CSS_SELECTOR, '[data-test*="@web/GlobalHeader/UtilityHeader/"]')
BENEFIT_CELLS =  (By.CSS_SELECTOR, "a[data-test='@web/slingshot-components/CellsComponent/Link']")



@given('Open target circle main page')
def open_main(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify there are at least 10 benefit cells')
def verify_benefit_cells(context):
     cells = context.driver.find_elements(*BENEFIT_CELLS)
     count = len(cells)
     print(f"Benefit cell links found: {count}")
     assert count >= 10, f"Expected at least 10 benefit cells, but found {count}"


@when('Search for {search_word}')
def search_product(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(7)


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()


