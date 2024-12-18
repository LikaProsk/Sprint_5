from time import sleep

import pytest
import auth_page_elements as auth_elements

from selenium.webdriver.common.by import By
from base_class import BaseClass
from home_page_elements import button_personal_account, constructor_button, element_make_burger, logo_element, \
    sauce_section_element


class TestConstructor(BaseClass):

    def test_constructor_button_access(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        self.send_keys(driver, auth_elements.element_email, "lika.proskurina@mail.ru")
        self.send_keys(driver, auth_elements.element_password, "parol123")
        self.click_element(driver, auth_elements.button_access)
        sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        self.click_element(driver, button_personal_account)
        sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

        self.click_element(driver, constructor_button)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        assert self.get_element_text(driver, element_make_burger) == 'Соберите бургер'

        driver.quit()

    def test_constructor_logo_access(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        self.send_keys(driver, auth_elements.element_email, "lika.proskurina@mail.ru")
        self.send_keys(driver, auth_elements.element_password, "parol123")
        self.click_element(driver, auth_elements.button_access)
        sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        self.click_element(driver, button_personal_account)
        sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

        self.click_element(driver, logo_element)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        assert self.get_element_text(driver, element_make_burger) == 'Соберите бургер'

        driver.quit()

    @pytest.mark.parametrize("section", ['Соусы', 'Булки', 'Начинки'])
    def test_bun_section_access(self, driver, section):
        section_element = (By.XPATH, f"//span[contains(text(), '{section}')]")

        driver.get("https://stellarburgers.nomoreparties.site/")

        if section == 'Булки':
            self.click_element(driver, sauce_section_element)

        self.click_element(driver, section_element)

        assert driver.find_element(By.XPATH, f"//h2[contains(text(), '{section}')]").is_displayed()

        driver.quit()
