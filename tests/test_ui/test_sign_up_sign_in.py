import pytest
from playwright.sync_api import Page
from pages.Sign_up_and_Sign_in import SignIn, SignUp



@pytest.mark.parametrize("role", ["producer", "blogger"])


def test_sign_up(page: Page, role: str):
    sign_up = SignUp(page)
    sign_up.open()
    sign_up.click_registration()
    sign_up.check_url_registration()
    sign_up.select_role(role)
    sign_up.enter_number()
    sign_up.check_tg_url_registration()
    sign_up.switch_to_iframe()
    sign_up.tg_button_visible()


def test_sign_in(page: Page):
    sign_up = SignUp(page)
    sign_in = SignIn(page)
    sign_up.open()
    sign_in.click_sign_in()
    sign_in.check_url_login()
    sign_in.switch_to_iframe()
    sign_in.tg_button_visible()

