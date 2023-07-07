import pytest
import pages
import time


class TestFooter:

    def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
        pages.index_page.open_index_page(page)
        actual_result = pages.index_page.get_text_from_google_search_button(page)
        time.sleep(10)
        assert actual_result == 'Google Search', 'Google search button is not correct'


