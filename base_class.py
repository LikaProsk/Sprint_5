from typing import Tuple
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from urls.site_urls import home_page_url


class BaseClass:

    def open_home_page(self, driver):
        driver.get(home_page_url)

    def click_element(self, driver, locator: Tuple[str, str]):
        driver.find_element(locator[0], locator[1]).click()

    def send_keys(self, driver, locator: Tuple[str, str], value: str):
        driver.find_element(locator[0], locator[1]).send_keys(value)

    def get_element_text(self, driver, locator: Tuple[str, str]):
        return driver.find_element(locator[0], locator[1]).text

    def get_element_attribute(self, driver, locator: Tuple[str, str], attribute_name: str):
        return driver.find_element(locator[0], locator[1]).get_attribute(attribute_name)
    
    def check_element_visibility_and_wait(self, driver, locator: Tuple[str, str], wait_time: int = 10):
        wait = WebDriverWait(driver, wait_time)
        element = wait.until(EC.visibility_of_element_located(locator))

        return element

    def is_element_displayed(self, driver, locator: Tuple[str, str]):
        return driver.find_element(locator[0], locator[1]).is_displayed()
