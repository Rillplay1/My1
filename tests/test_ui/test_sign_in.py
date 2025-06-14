from playwright.sync_api import Page
from pages.Sign_In import SignIn
from pages.Sign_Up import SignUp
import allure

@allure.feature("Авторизация")
@allure.story("Авторизация через главную страницу")
def test_sign_in(page: Page):
    sign_in = SignIn(page)
    sign_up = SignUp(page)
    sign_in.open()
    sign_in.click_sign_in()
    sign_in.check_url_login()
    sign_up.switch_to_iframe()
    sign_up.tg_button_visible()

