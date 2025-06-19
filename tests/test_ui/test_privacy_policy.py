from playwright.sync_api import Page
from pages.Privacy_policy import PrivacyPolicy
import allure


@allure.feature("Политика конфиденциальности test")
@allure.story("Кликнуть на политику конфиденциальности test")
def test_offer_agreement(page: Page):
    offer_agreement = PrivacyPolicy(page)
    offer_agreement.open()
    offer_agreement.click_privacy_policy()
    offer_agreement.check_privacy_policy_url()
    offer_agreement.check_privacy_policy_text()