
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# @pytest.fixture()
# def browser():
#         chrome_browser = webdriver.Chrome()
#         chrome_browser.maximize_window()
#         yield chrome_browser
#         chrome_browser.quit()












@pytest.fixture()
def browser():
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
        yield driver
        driver.quit()