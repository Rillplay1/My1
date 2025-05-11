from playwright.sync_api import Page
from pages.Sign_up_and_Sign_in import SmokeTests
from pages.regress import Cases, Blog, AboutUs, TgSupport


def test_cases(page: Page):
    smoke = SmokeTests(page)
    cases = Cases(page)
    smoke.open()
    cases.click_cases()
    cases.check_cases_url()
    cases.check_cases_text()



def test_blog(page: Page):
    smoke = SmokeTests(page)
    blog = Blog(page)
    smoke.open()
    blog.click_blog()
    blog.check_blog_url()


def test_about_us(page: Page):
    smoke = SmokeTests(page)
    about_us = AboutUs(page)
    smoke.open()
    about_us.click_about_us()
    about_us.check_about_us_url()


def test_tg(page: Page):
    smoke = SmokeTests(page)
    tg_support = TgSupport(page)
    smoke.open()
    tg_support.click_tg_support_check_url()

