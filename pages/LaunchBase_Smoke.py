from playwright.sync_api import Page, expect
from config.logger import logger

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def get_url(self) -> str:
        return self.page.url



class SmokeTests(BasePage):
    def open(self):
        self.page.goto("https://launch-base.online/")
        logger.info("Открываем главную страницу")

    def click_registration(self):
        self.page.locator('a[href="/registration"]').nth(0).click()
        logger.info("Кликаем на регистрацию")

    def check_url_registration(self):
        expect(self.page).to_have_url("https://launch-base.online/registration")

    def registration_path(self, role):
        self.page.locator(f'//img[@alt="{role}"]').click()
        self.page.locator('//a[@href="/sign-up"]').click()
        logger.info("Выбрали роль и кликнуть далее")
        self.page.locator('//input[@name="phone"]').fill("79999999999")
        self.page.locator('(//button[@type="submit"])[1]').click()
        logger.info("Вести номер телефона и нажать далее")


    def check_tg_url_registration(self):
        expect(self.page).to_have_url("https://launch-base.online/last-step")

    def switch_to_iframe(self):
        self.iframe = self.page.frame_locator("iframe").first

    def tg_button_visible(self):
        button = self.iframe.locator('//button[@class="btn tgme_widget_login_button"]')
        expect(button).to_be_visible()


class LoginPage(SmokeTests):
    def click_sign_in(self):
        self.page.locator('a[href="/login"]').nth(0).click()
        logger.info("Кликнуть на авторизацию")

    def check_url_login(self):
        expect(self.page).to_have_url("https://launch-base.online/login")