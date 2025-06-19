import pytest
from playwright.sync_api import Page
from pages.Sign_Up import SignUp
import allure


@pytest.mark.parametrize("role", ["producer", "blogger"])


@allure.feature("Регистрация блогер или эксперт")
@allure.story("Регистрация через главную страницу")
def test_sign_up(page: Page, role: str):
    sign_up = SignUp(page)
    sign_up.open()
    sign_up.click_registration()
    sign_up.check_url_registration()
    sign_up.select_role(role)
    sign_up.enter_number()
    sign_up.check_tg_url_registration()
    sign_up.tg_button_visible()
