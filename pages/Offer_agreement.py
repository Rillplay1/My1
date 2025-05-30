import allure
from playwright.sync_api import expect
from pages.Base_page import BasePage


class OfferAgreement(BasePage):
    @allure.step("Кликнуть на 'Договор оферты'")
    def click_offer_agreement(self):
        self.page.locator('(//a[@href="/terms-offer"])[1]').click()

    @allure.step("Проверка юрла на странице")
    def check_agreement_url(self):
        expect(self.page).to_have_url("https://launch-base.online/terms-offer")

    @allure.step("Проверка что текст 'ДОГОВОР-ОФЕРТА' присутствует на странице")
    def check_agreement_text(self):
        expect(self.page.get_by_text("ДОГОВОР-ОФЕРТА")).to_be_visible()





