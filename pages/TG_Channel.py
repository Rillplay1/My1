import allure
from pages.Base_page import BasePage
from playwright.sync_api import expect


class TgChannel(BasePage):
    def click_tg_channel_check_url(self):
        with self.page.expect_popup() as popup_info:
            with allure.step("Нажать на значок тг канала"):
                self.page.locator('(//a[@href="https://t.me/launch_base_ru"])[2]').click()
            popup = popup_info.value
            with allure.step("Проверка что открывается окно с тг каналом"):
                expect(popup).to_have_url("https://t.me/launch_base_ru")









