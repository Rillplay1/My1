import allure
from pages.Base_page import BasePage
from playwright.sync_api import expect


class Cases(BasePage):
    @allure.step("Нажать на раздел кейсы")
    def click_cases(self):
        self.page.locator('(//a[@href="/successful-outcomes-and-experience"])[1]').click()

    @allure.step("Проверка URL на странице кейсов")
    def check_cases_url(self):
        expect(self.page).to_have_url("https://launch-base.online/successful-outcomes-and-experience")

    @allure.step("Проверка текста на странице кейсов")
    def check_cases_text(self):
        expect(self.page.get_by_text("Успешные кейсы на LaunchBase")).to_be_visible()
