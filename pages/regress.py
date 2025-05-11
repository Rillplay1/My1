import allure

from pages.Sign_up_and_Sign_in import BasePage
from playwright.sync_api import expect




class Cases(BasePage):
    @allure.step("Нажать на раздел кейсы")
    def click_cases(self):
        self.page.locator('(//a[@href="/successful-outcomes-and-experience"])[1]').click()

    @allure.step("Проверка юрла на странице кейсов")
    def check_cases_url(self):
        expect(self.page).to_have_url("https://launch-base.online/successful-outcomes-and-experience")

    @allure.step("Проверка текста на странице кейсов")
    def check_cases_text(self):
        expect(self.page.get_by_text("Успешные кейсы на LaunchBase")).to_be_visible()



class Blog(BasePage):
    @allure.step("Нажать на раздел блог")
    def click_blog(self):
        self.page.locator('//a[@href="/blog"]').click()

    @allure.step("Проверка юрла на странице блога")
    def check_blog_url(self):
        expect(self.page).to_have_url("https://launch-base.online/blog")



class AboutUs(BasePage):
    @allure.step("Нажать на раздел о нас")
    def click_about_us(self):
        self.page.locator('//a[@href="/about"]').click()

    @allure.step("Проверка юрла на странице о нас")
    def check_about_us_url(self):
        expect(self.page).to_have_url("https://launch-base.online/about")



class TgSupport(BasePage):
    def click_tg_support_check_url(self):
        with self.page.expect_popup() as popup_info:
            with allure.step("Нажать на значок поддержки тг"):
                self.page.locator('(//a[@href="https://t.me/Launch_Base"])[1]').click()
            popup = popup_info.value
            with allure.step("Проверка что открывается окно с тг"):
                expect(popup).to_have_url("https://t.me/Launch_Base")









