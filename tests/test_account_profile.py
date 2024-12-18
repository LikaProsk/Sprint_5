import auth_page_elements as auth_elements

from time import sleep
from base_class import BaseClass
from home_page_elements import button_personal_account
from private_account_page_elements import user_name, user_email


class TestAccountProfile(BaseClass):

    def test_account_profile_access(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        self.send_keys(driver, auth_elements.element_email, "lika.proskurina@mail.ru")
        self.send_keys(driver, auth_elements.element_password, "parol123")
        self.click_element(driver, auth_elements.button_access)
        sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        self.click_element(driver, button_personal_account)
        sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
        assert self.get_element_attribute(driver, user_name, 'value') == 'Lika'
        assert self.get_element_attribute(driver, user_email, 'value') == 'lika.proskurina@mail.ru'

        driver.quit()
