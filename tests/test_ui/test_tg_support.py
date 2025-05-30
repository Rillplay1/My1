from playwright.sync_api import Page
from pages.TG_Support import TgSupport


def test_tg_support(page: Page):
    tg_support = TgSupport(page)
    tg_support.open()
    tg_support.click_tg_support_check_url()


