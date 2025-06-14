import allure
from playwright.sync_api import expect
from pages.Base_page import BasePage


class PrivacyPolicy(BasePage):
    @allure.step("Кликнуть на 'Политику конфиденциальности'")
    def click_privacy_policy(self):
        self.page.locator('//a[@href="/policy"]').click()

    @allure.step("Проверка URL на странице")
    def check_privacy_policy_url(self):
        expect(self.page).to_have_url("https://launch-base.online/policy")

    @allure.step("Проверка что текст 'Политика конфиденциальности' присутствует на странице")
    def check_privacy_policy_text(self):
        expect(self.page.get_by_text("Политика конфиденциальности").nth(0)).to_be_visible()