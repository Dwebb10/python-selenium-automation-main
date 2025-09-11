from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('open Target homepage')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('user clicks on the Sign In link')
def click_sign_in_link(context):
    context.driver.find_element(By.ID, "account-sign-in").click()
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()



@then('verify sign in page shows')
def verify_signin_page(context):
    username_field = context.driver.find_element(By.ID, 'username')
    assert username_field.is_displayed()
    (sleep(7))