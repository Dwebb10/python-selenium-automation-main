from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    GRID       = (By.CSS_SELECTOR, '[data-test="@web/ProductGrid"]')
    TITLES     = (By.CSS_SELECTOR, '[data-test="product-title"] a, [data-test="product-title"]')
    HEADING    = (By.CSS_SELECTOR, '[data-test="resultsHeading"], h1, h2')
    RESULT_ANY = (By.CSS_SELECTOR, '[data-test="product-title"], [data-test="@web/ProductCard"]')

    def wait_loaded(self):
        # 1) wait URL indicates a search
        self.wait.until(lambda d: "/s?" in d.current_url or "searchTerm=" in d.current_url)
        # 2) wait for any of known result markers
        for loc in (self.GRID, self.TITLES, self.HEADING, self.RESULT_ANY):
            try:
                self.wait.until(EC.presence_of_any_elements_located(loc))
                return
            except Exception:
                continue

        self.wait.until(EC.presence_of_all_elements_located(self.RESULT_ANY))

