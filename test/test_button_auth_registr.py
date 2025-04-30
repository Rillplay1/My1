from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.registration_locators import RegistrationLocators


#Переменые
def open_url(browser):
    browser.get("https://launch-base.online/")

def wait_reg(browser, button_xpath):
    wait = WebDriverWait(browser, 15)
    wait.until(lambda _: browser.execute_script("return document.readyState") == "complete")
    wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath))).click()
    wait.until(EC.url_contains("/registration"))

def wait_login(browser, login_xpath):
    wait = WebDriverWait(browser, 15)
    wait.until(lambda _: browser.execute_script("return document.readyState") == "complete")
    wait.until(EC.element_to_be_clickable((By.XPATH, login_xpath))).click()
    wait.until(EC.url_contains("/login"))
#Переменые



@pytest.mark.parametrize("button_xpath", [
'(//a[@href="/registration"])[1]',
'(//a[@href="/registration"])[2]',
'(//a[@href="/registration"])[3]',
])
def test_registr_bottons(browser, button_xpath):
    open_url(browser)
    wait_reg(browser, button_xpath)
    expected_url = "https://launch-base.online/registration"

    assert expected_url in browser.current_url, f"Ожидался переход на {expected_url}, но был {browser.current_url}"


@pytest.mark.parametrize("login_xpath", [
'(//a[@href="/login"])[1]',
'(//a[@href="/login"])[2]'
])
def test_button_login(browser, login_xpath):
    open_url(browser)
    wait_login(browser, login_xpath)
    expected_url = "https://launch-base.online/login"

    assert expected_url in browser.current_url, f"Ожидался переход на {expected_url}, но был {browser.current_url}"



def test_button3_registr(browser):
        open_url(browser)
        wait = WebDriverWait(browser, 15)
        wait.until(lambda _: browser.execute_script("return document.readyState") == "complete")

        wait.until(EC.element_to_be_clickable(RegistrationLocators.REGISTER_BTN3)).click()
        expected_url = "https://launch-base.online/registration"
        wait.until(EC.url_to_be(expected_url))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//img[@alt="blogger"]'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/sign-up"]'))).click()

        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="phone"]'))).send_keys("999 999-99-99")
        wait.until(EC.element_to_be_clickable((By.XPATH, '(//*[@type="submit"])[1]'))).click()
        expected_url = "https://launch-base.online/last-step"
        wait.until(EC.url_to_be(expected_url))
        wait.until(lambda _: browser.execute_script("return document.readyState") == "complete")
        assert (EC.presence_of_element_located((By.XPATH, '//*[@onclick="return TWidgetLogin.auth();"]')))

def test_button4_registr(browser):
    open_url(browser)
    wait = WebDriverWait(browser, 15)
    wait.until(lambda _: browser.execute_script("return document.readyState") == "complete")

    wait.until(EC.element_to_be_clickable(RegistrationLocators.REGISTER_BTN4)).click()
    expected_url = "https://launch-base.online/registration"
    wait.until(EC.url_to_be(expected_url))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//img[@alt="producer"]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/sign-up"]'))).click()

    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="phone"]'))).send_keys("999 999-99-99")
    wait.until(EC.element_to_be_clickable((By.XPATH, '(//*[@type="submit"])[1]'))).click()
    expected_url = "https://launch-base.online/last-step"
    wait.until(EC.url_to_be(expected_url))
    wait.until(lambda _: browser.execute_script("return document.readyState") == "complete")
    assert (EC.presence_of_element_located((By.XPATH, '//*[@onclick="return TWidgetLogin.auth();"]')))




