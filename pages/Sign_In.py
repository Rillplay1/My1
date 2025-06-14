import allure
from playwright.sync_api import expect
from pages.Base_page import BasePage


class SignIn(BasePage):
    @allure.feature("Авторизация")
    @allure.step("Кликнуть на авторизацию")
    def click_sign_in(self):
        self.page.locator('a[href="/login"]').nth(0).click()


    @allure.step("Проверка URL на странице логина")
    def check_url_login(self):
        expect(self.page).to_have_url("https://launch-base.online/login")

