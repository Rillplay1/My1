import allure
from playwright.sync_api import expect
from pages.Base_page import BasePage


class SignUp(BasePage):
    @allure.step("Кликнуть на регистрацию")
    def click_registration(self):
        self.page.locator('a[href="/registration"]').nth(0).click()

    @allure.step("Проверка юрл регистрации")
    def check_url_registration(self):
        expect(self.page).to_have_url("https://launch-base.online/registration")

    def select_role (self, role):
        with allure.step("Выбрать роль"):
            self.page.locator(f'//img[@alt="{role}"]').click()
        with allure.step("Нажать продолжить"):
            self.page.locator('//a[@href="/sign-up"]').click()
    def enter_number(self):
        with allure.step("Ввести номер телефона"):
            self.page.locator('//input[@name="phone"]').fill("79999999999")
        with allure.step("Нажать далее"):
            self.page.locator('(//button[@type="submit"])[1]').click()

    @allure.step("Проверка юрла регистрации (окно с тг)")
    def check_tg_url_registration(self):
        expect(self.page).to_have_url("https://launch-base.online/last-step")

    def switch_to_iframe(self):
        self.iframe = self.page.frame_locator("iframe").first

    @allure.step("Проверка что кнопка регистрации через тг видна")
    def tg_button_visible(self):
        button = self.iframe.locator('//button[@class="btn tgme_widget_login_button"]')
        expect(button).to_be_visible()
