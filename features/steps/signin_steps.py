from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC

def w(ctx, t=12): return W(ctx.driver, t)

@given('open Target homepage')
def open_home(ctx):
    ctx.driver.get('https://www.target.com/')

@when('user clicks on the Sign In link')
def click_sign_in(ctx):
    # Open account menu (several variants)
    CANDIDATES = [
        (By.CSS_SELECTOR, '[data-test="@web/AccountLink"]'),
        (By.ID, 'account-sign-in'),
        (By.CSS_SELECTOR, '[aria-label*="Account"]'),
    ]
    opened = False
    for by, locator in CANDIDATES:
        try:
            w(ctx, 8).until(EC.element_to_be_clickable((by, locator))).click()
            opened = True
            break
        except Exception:
            continue
    assert opened, "Could not open account menu in header."


    SIGNIN = (By.XPATH, "//a[contains(., 'Sign in') or contains(., 'Sign In')] | //button[contains(., 'Sign in') or contains(., 'Sign In')]")
    w(ctx, 8).until(EC.element_to_be_clickable(SIGNIN)).click()

@then('verify sign in page shows')
def verify_signin(ctx):
    USERNAME = (By.ID, 'username')
    assert w(ctx, 10).until(EC.visibility_of_element_located(USERNAME))


