from behave import given, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC

def w(ctx, t=12): return W(ctx.driver, t)

CELLS = (
    By.CSS_SELECTOR,
    "a[data-test='@web/slingshot-components/CellsComponent/Link'], "
    "[data-test*='CellsComponent'] a, "
    "a[href*='/circle/']"
)

@given('Open target circle main page')
def open_circle(ctx):
    ctx.driver.get('https://www.target.com/circle')

@then('Verify there are at least 10 benefit cells')
def verify_benefit_cells(ctx):
    try:
        w(ctx, 10).until(EC.presence_of_all_elements_located(CELLS))
    except Exception:
        pass

    last = 0
    for _ in range(6):
        ctx.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            w(ctx, 3).until(lambda d: len(d.find_elements(*CELLS)) > last)
            last = len(ctx.driver.find_elements(*CELLS))
        except Exception:
            break

    count = len(ctx.driver.find_elements(*CELLS))
    assert count >= 10, f"Expected at least 10 benefit cells, found {count}"




