from selenium.webdriver.common.by import By
import time
from pages.homepage import HomePage
from pages.product import ProductPage


def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    products = ProductPage(driver)
    ProductPage.check_title_is('Samsung galaxy s6')



def test_monitors (driver):
        driver.get("https://www.demoblaze.com/")
        monitor_link = driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
        monitor_link.click()
        time.sleep(3)
        monitors = driver.find_elements(By.CSS_SELECTOR, '.card')
        assert len(monitors) == 2
