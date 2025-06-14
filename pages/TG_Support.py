import allure
from pages.Base_page import BasePage
from playwright.sync_api import expect


class TgSupport(BasePage):
    def click_tg_support_check_url(self):
        with self.page.expect_popup() as popup_info:
            with allure.step("Нажать на значок поддержки Telegram"):
                self.page.locator('(//a[@href="https://t.me/Launch_Base"])[2]').click()
            popup = popup_info.value
            with allure.step("Проверка что открывается окно с Telegram"):
                expect(popup).to_have_url("https://t.me/Launch_Base")
