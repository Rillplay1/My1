from playwright.sync_api import Page
from pages.Cases import Cases


def test_cases(page: Page):
    cases = Cases(page)
    cases.open()
    cases.click_cases()
    cases.check_cases_url()
    cases.check_cases_text()