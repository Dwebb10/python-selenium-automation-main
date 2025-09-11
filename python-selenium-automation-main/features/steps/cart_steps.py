from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Search for a Product')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('hat')
    sleep(7)

@then('Verify product exists')
def verify_product(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']")
    expected_text = 'hat'
    assert expected_text in actual_text, f'Error. Expected text {expected_text}'