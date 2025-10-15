from behave import given, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

COLOR_OPTIONS   = (By.CSS_SELECTOR, "li[class*='CarouselItem'] img")
SELECTED_COLOR  = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")

def wait(driver, timeout=15):
    return WebDriverWait(driver, timeout)

@given('Open target product A-91269718 page')
def open_target(context):
    context.driver.get(
        "https://www.target.com/p/wranglers-men-39-s-relaxed-fit-straight-jeans/-/A-91269718?preselect=90919011#lnk=sametab"
    )
    wait(context.driver).until(EC.presence_of_all_elements_located(COLOR_OPTIONS))

@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Navy Denim', 'Dark Wash', 'Light Wash']

    w = wait(context.driver)
    colors = w.until(EC.presence_of_all_elements_located(COLOR_OPTIONS))
    assert colors, "No color options found on the product page."

    actual_colors = []
    for idx in range(len(colors)):
        # Re-find each loop to avoid stale references after click/DOM update
        current = context.driver.find_elements(*COLOR_OPTIONS)
        el = current[idx]

        context.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        w.until(EC.element_to_be_clickable(el)).click()

        selected_el = w.until(EC.visibility_of_element_located(SELECTED_COLOR))
        parts = [p.strip() for p in selected_el.text.split("\n") if p.strip()]
        chosen = parts[-1] if parts else ""
        actual_colors.append(chosen)

    print("Clicked colors:", actual_colors)
    assert expected_colors == actual_colors, \
        f"Expected {expected_colors} but got {actual_colors}"