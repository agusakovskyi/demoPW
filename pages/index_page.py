from playwright.sync_api import Page
import config
from fixtures import page


class IndexPage:
    BUTTON_GOOGLE_SEARCH = "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']"
    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    def get_text_from_google_search_button(self, page: Page) -> None:
        return page.locator(self.BUTTON_GOOGLE_SEARCH).get_attribute('value')