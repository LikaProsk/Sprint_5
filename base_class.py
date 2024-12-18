from selenium.webdriver.common.by import By


class BaseClass:

    def open_home_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

    def click_element(self, driver, locator: tuple):
        driver.find_element(locator[0], locator[1]).click()

    def send_keys(self, driver, locator: tuple, value: str):
        driver.find_element(locator[0], locator[1]).send_keys(value)

    def get_element_text(self, driver, locator: tuple):
        return driver.find_element(locator[0], locator[1]).text

    def get_element_attribute(self, driver, locator: tuple, attribute_name: str):
        return driver.find_element(locator[0], locator[1]).get_attribute(attribute_name)
