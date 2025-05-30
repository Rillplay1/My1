from playwright.sync_api import Page
from pages.TG_Channel import TgChannel


def test_tg_channel(page: Page):
    tg_channel = TgChannel(page)
    tg_channel.open()
    tg_channel.click_tg_channel_check_url()