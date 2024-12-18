import random
import pytest
import reg_page_elements as reg_elements
import auth_page_elements as auth_element

from time import sleep
from base_class import BaseClass
from forgot_password_page_elements import access_button
from home_page_elements import button_personal_account, button_account_access
from private_account_page_elements import logout_button


class TestAuthorization(BaseClass):

    @pytest.mark.parametrize("auth_button", [button_personal_account,
                                             button_account_access],
                             ids=['Personal account button access test', 'Account access button test'])
    def test_home_page_buttons_auth(self, driver, auth_button):
        self.open_home_page(driver)
        self.click_element(driver, auth_button)
        sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

        self.send_keys(driver, auth_element.element_email, "lika.proskurina@mail.ru")
        self.send_keys(driver, auth_element.element_password, "parol123")
        self.click_element(driver, auth_element.button_access)
        sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()

    def test_registration_form_auth(self, driver):
        names = ['Lika', 'Ivan', 'Petr', 'Roman']
        driver.get("https://stellarburgers.nomoreparties.site/register")
        name = names[random.randint(0, len(names) - 1)]
        email = f"{name}{random.randint(0, 10000)}@mail.ru"

        password = "parol123"

        self.send_keys(driver, reg_elements.element_name, name)
        self.send_keys(driver, reg_elements.element_email, email)
        self.send_keys(driver, reg_elements.element_password, password)
        self.click_element(driver, reg_elements.button_registration)
        sleep(0.5)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

        self.send_keys(driver, auth_element.element_email, email)
        self.send_keys(driver, auth_element.element_password, password)
        self.click_element(driver, auth_element.button_access)
        sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()

    def test_password_restore_button(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        self.click_element(driver, access_button)
        sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

        self.send_keys(driver, auth_element.element_email, "lika.proskurina@mail.ru")
        self.send_keys(driver, auth_element.element_password, "parol123")
        self.click_element(driver, auth_element.button_access)
        sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()

    def test_account_logout(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        self.send_keys(driver, auth_element.element_email, "lika.proskurina@mail.ru")
        self.send_keys(driver, auth_element.element_password, "parol123")
        self.click_element(driver, auth_element.button_access)
        sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        self.click_element(driver, button_personal_account)
        sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

        self.click_element(driver, logout_button)
        sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

        driver.quit()
