import allure
from playwright.sync_api import expect
from pages.Base_page import BasePage


class SignUp(BasePage):
    @allure.step("Кликнуть на регистрацию")
    def click_registration(self):
        self.page.locator('a[href="/registration"]').nth(0).click()


    @allure.step("Проверка  регистрации")
    def check_url_registration(self):
        expect(self.page).to_have_url("https://launch-base.online/registration")


    def select_role (self, role):
        with allure.step("Выбрать роль"):
            self.page.locator(f'//img[@alt="{role}"]').click()
        with allure.step("Нажать продолжить"):
            self.page.locator('//a[@href="/sign-up"]').click()


    def enter_number(self):
        with allure.step("Ввести номер Nтелефона"):
            self.page.locator('//input[@name="phone"]').fill("79999999999")
        with allure.step("Нажать далее"):
            self.page.locator('(//button[@type="submit"])[1]').click()


    @allure.step("Проверка URL регистрации (окно с Telegram)")
    def check_tg_url_registration(self):
        expect(self.page).to_have_url("https://launch-base.online/last-step")


    def __get_iframe(self):
        return self.page.frame_locator("iframe").first


    @allure.step("Проверка что кнопка регистрации через Telegram видна")
    def tg_button_visible(self):
        button = self.__get_iframe().locator('//button[@class="btn tgme_widget_login_button"]')
        expect(button).to_be_visible()




