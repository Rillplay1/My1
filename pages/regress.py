from pages.LaunchBase_Smoke import BasePage
from playwright.sync_api import expect



class Cases(BasePage):
    def click_cases(self):
        self.page.locator('(//a[@href="/successful-outcomes-and-experience"])[1]').click()

    def check_cases_url(self):
        expect(self.page).to_have_url("https://launch-base.online/successful-outcomes-and-experience")

    def check_cases_text(self):
        expect(self.page.get_by_text("Успешные кейсы на LaunchBase")).to_be_visible()



class Blog(BasePage):
    def click_blog(self):
        self.page.locator('//a[@href="/blog"]').click()

    def check_blog_url(self):
        expect(self.page).to_have_url("https://launch-base.online/blog")



class AboutUs(BasePage):
    def click_about_us(self):
        self.page.locator('//a[@href="/about"]').click()

    def check_about_us_url(self):
        expect(self.page).to_have_url("https://launch-base.online/about")



class TgSupport(BasePage):
    def click_tg_support_check_url(self):
        with self.page.expect_popup() as popup_info:
            self.page.locator('(//a[@href="https://t.me/Launch_Base"])[1]').click()
            popup = popup_info.value
            expect(popup).to_have_url("https://t.me/Launch_Base")









