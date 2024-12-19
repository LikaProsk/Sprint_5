from data.test_data import auth_email, password, auth_login
from locators import auth_page_elements as auth_elements

from base_class import BaseClass
from locators.home_page_elements import button_personal_account, bun_section_element
from locators.private_account_page_elements import user_name, user_email, logout_button
from urls.site_urls import auth_url, home_page_url, acc_profile_page


class TestAccountProfile(BaseClass):

    def test_account_profile_access(self, driver):
        driver.get(auth_url)
        self.send_keys(driver, auth_elements.element_email, auth_email)
        self.send_keys(driver, auth_elements.element_password, password)
        self.click_element(driver, auth_elements.button_access)
        self.check_element_visibility_and_wait(driver, bun_section_element)

        assert driver.current_url == home_page_url

        self.click_element(driver, button_personal_account)
        self.check_element_visibility_and_wait(driver, logout_button)

        assert driver.current_url == acc_profile_page
        assert self.get_element_attribute(driver, user_name, 'value') == auth_login
        assert self.get_element_attribute(driver, user_email, 'value') == auth_email

