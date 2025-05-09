import pytest
from playwright.sync_api import Page
from pages.LaunchBase_Smoke import SmokeTests, LoginPage



@pytest.mark.parametrize("role", ["producer", "blogger"])


def test_sign_up(page: Page, role: str):
    smoke_tests = SmokeTests(page)
    smoke_tests.open()
    smoke_tests.click_registration()
    smoke_tests.registration_path(role)
    smoke_tests.check_tg_url_registration()
    smoke_tests.switch_to_iframe()
    smoke_tests.tg_button_visible()



def test_sign_in(page: Page):
    smoke_tests = SmokeTests(page)
    login_page = LoginPage(page)
    smoke_tests.open()
    login_page.click_sign_in()
    login_page.check_url_login()
    smoke_tests.switch_to_iframe()
    smoke_tests.tg_button_visible()

