# features/steps/Product_loop.py
from behave import given, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def w(ctx, t=12):
    return W(ctx.driver, t)

# Common variations of color swatch locators (Target A/B tests a lot)
SWATCH_LOCATORS = [
    # aria radios for colors
    (By.CSS_SELECTOR, '[role="radio"][aria-label*="Color" i]'),
    (By.CSS_SELECTOR, '[role="radio"][aria-label*="colour" i]'),
    (By.CSS_SELECTOR, '[data-test*="Swatch"] [role="radio"]'),
    (By.CSS_SELECTOR, '[data-test*="Color"] [role="radio"]'),
    (By.CSS_SELECTOR, '[data-test*="Variation"] [role="radio"]'),
    # img/button inside radio li
    (By.CSS_SELECTOR, 'li[role="radio"] button, li[role="radio"] img, li[role="radio"]'),
]

# Label that shows currently selected color (several variants)
SELECTED_COLOR_LABELS = [
    (By.CSS_SELECTOR, '[data-test="@web/VariationComponent"] [data-test*="Color" i]'),
    (By.CSS_SELECTOR, '[data-test*="Variation"] [data-test*="Color" i]'),
    (By.CSS_SELECTOR, '[data-test*="color" i]'),
]

COOKIE_ACCEPT = (By.ID, "onetrust-accept-btn-handler")

def _accept_cookies_if_any(ctx):
    try:
        btn = w(ctx, 3).until(EC.element_to_be_clickable(COOKIE_ACCEPT))
        btn.click()
    except Exception:
        pass  # no banner

def _find_first_with_results(ctx, locators):
    """
    Try all provided locators; return the first list of elements with len>=2.
    """
    for by, sel in locators:
        try:
            w(ctx, 8).until(EC.presence_of_all_elements_located((by, sel)))
            els = [e for e in ctx.driver.find_elements(by, sel) if e.is_displayed()]
            if len(els) >= 2:
                return (by, sel), els
        except TimeoutException:
            continue
    return None, []

def _read_selected_color(ctx):
    # Try dedicated labels first
    for by, sel in SELECTED_COLOR_LABELS:
        try:
            el = w(ctx, 2).until(EC.visibility_of_element_located((by, sel)))
            txt = el.text.strip()
            if txt:
                # Common pattern: "Color\nNavy Denim" -> keep last line
                parts = [p.strip() for p in txt.splitlines() if p.strip()]
                return parts[-1] if parts else txt
        except Exception:
            continue
    # Fallback: count any aria-checked radios
    try:
        checked = ctx.driver.find_elements(By.CSS_SELECTOR, '[role="radio"][aria-checked="true"]')
        if checked:
            return checked[0].get_attribute("aria-label") or "selected"
    except Exception:
        pass
    return ""

@given('Open target product A-91269718 page')
def open_product(ctx):
    ctx.driver.get('https://www.target.com/p/wranglers-men-39-s-relaxed-fit-straight-jeans/-/A-91269718?preselect=90919011#lnk=sametab')
    _accept_cookies_if_any(ctx)

@then('Verify user can click through colors')
def click_and_verify_colors(ctx):
    # Find swatches using robust fallbacks
    used_locator, swatches = _find_first_with_results(ctx, SWATCH_LOCATORS)
    assert swatches, "Could not locate color swatches (Target DOM likely changed)."

    seen = []
    for i in range(len(swatches)):
        # Refetch each loop to avoid stale elements after DOM updates
        _, current = _find_first_with_results(ctx, [used_locator]) if used_locator else (None, [])
        if not current:
            _, current = _find_first_with_results(ctx, SWATCH_LOCATORS)
        if not current:
            break

        # Bound i if list shrank
        idx = min(i, len(current) - 1)
        el = current[idx]

        # Scroll into view & try normal click, then JS click as fallback
        try:
            ctx.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        except Exception:
            pass
        try:
            el.click()
        except Exception:
            try:
                ctx.driver.execute_script("arguments[0].click();", el)
            except Exception:
                continue  # try next one

        # Wait for selection to register either via aria-checked or label change
        selected_ok = False
        try:
            w(ctx, 6).until(lambda d: el.get_attribute("aria-checked") == "true")
            selected_ok = True
        except Exception:
            # try reading selected color label text change
            new_name = _read_selected_color(ctx)
            if new_name and (not seen or new_name != seen[-1]):
                selected_ok = True

        # Record selected color label if we can read it
        color_name = _read_selected_color(ctx)
        if color_name:
            if not seen or seen[-1] != color_name:
                seen.append(color_name)

        assert selected_ok, "Swatch click did not toggle selection state."

    # Expect at least 2 distinct selections (tune to 3 if needed)
    assert len(seen) >= 2, f"Expected to select >=2 colors; got {len(seen)} ({seen})"

