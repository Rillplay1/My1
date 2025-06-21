import allure
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открываемм главную страницу")
    def open(self):
        self.page.goto("https://launch-base.online/")
