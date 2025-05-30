from playwright.sync_api import Page
from pages.Offer_agreement import OfferAgreement



def test_offer_agreement(page: Page):
    offer_agreement = OfferAgreement(page)
    offer_agreement.open()
    offer_agreement.click_offer_agreement()
    offer_agreement.check_agreement_url()
    offer_agreement.check_agreement_text()

