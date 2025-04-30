from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture()
def browser():
        chrome_browser = webdriver.Chrome()
        chrome_browser.maximize_window()
        yield chrome_browser
        chrome_browser.quit()


def test_button_clicked(browser):
        browser.get("https://launch-base.online/")
        wait = WebDriverWait(browser,10)
        wait.until(EC.presence_of_element_located((By.XPATH, '(//a[@href="/registration"])[1]')))
        registration_click = wait.until(EC.element_to_be_clickable((By.XPATH,'(//a[@href="/registration"])[1]')))


        assert registration_click.get_attribute(
            "href") == "https://launch-base.online/registration"


# def test_button_exites(browser):
#        browser.get("https://launch-base.online/")
#        assert browser.find_element(By.XPATH, "//*[@class='text-center flex items-center justify-center button-cr h-10 py-2 px-[1.125rem] rounded-md text-sm font-semibold w-min']")

