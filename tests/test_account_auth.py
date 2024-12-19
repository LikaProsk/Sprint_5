import pytest

from data.test_data import auth_email, password
from locators import reg_page_elements as reg_elements, auth_page_elements as auth_element
from base_class import BaseClass
from locators.auth_page_elements import button_access
from locators.forgot_password_page_elements import access_button
from locators.home_page_elements import button_personal_account, button_account_access, bun_section_element
from locators.private_account_page_elements import logout_button
from urls.site_urls import auth_url, home_page_url, reg_page_url, forgot_password_page_url, acc_profile_page


class TestAuthorization(BaseClass):

    @pytest.mark.parametrize("auth_button", [button_personal_account,
                                             button_account_access],
                             ids=['Personal account button access test', 'Account access button test'])
    def test_home_page_buttons_auth(self, driver, auth_button):
        self.open_home_page(driver)
        self.click_element(driver, auth_button)
        self.check_element_visibility_and_wait(driver, button_access)

        assert driver.current_url == auth_url

        self.send_keys(driver, auth_element.element_email, auth_email)
        self.send_keys(driver, auth_element.element_password, password)
        self.click_element(driver, auth_element.button_access)
        self.check_element_visibility_and_wait(driver, bun_section_element)

        assert driver.current_url == home_page_url

    def test_registration_form_auth(self, driver, reg_name, reg_email):

        driver.get(reg_page_url)

        self.send_keys(driver, reg_elements.element_name, reg_name)
        self.send_keys(driver, reg_elements.element_email, reg_email)
        self.send_keys(driver, reg_elements.element_password, password)
        self.click_element(driver, reg_elements.button_registration)
        self.check_element_visibility_and_wait(driver, button_access)

        assert driver.current_url == auth_url

        self.send_keys(driver, auth_element.element_email, reg_email)
        self.send_keys(driver, auth_element.element_password, password)
        self.click_element(driver, auth_element.button_access)
        self.check_element_visibility_and_wait(driver, bun_section_element)

        assert driver.current_url == home_page_url


    def test_password_restore_button(self, driver):
        driver.get(forgot_password_page_url)
        self.click_element(driver, access_button)
        self.check_element_visibility_and_wait(driver, button_access)

        assert driver.current_url == auth_url

        self.send_keys(driver, auth_element.element_email, auth_email)
        self.send_keys(driver, auth_element.element_password, password)
        self.click_element(driver, auth_element.button_access)
        self.check_element_visibility_and_wait(driver, bun_section_element)

        assert driver.current_url == home_page_url


    def test_account_logout(self, driver):
        driver.get(auth_url)
        self.send_keys(driver, auth_element.element_email, auth_email)
        self.send_keys(driver, auth_element.element_password, password)
        self.click_element(driver, auth_element.button_access)
        self.check_element_visibility_and_wait(driver, bun_section_element)

        assert driver.current_url == home_page_url

        self.click_element(driver, button_personal_account)
        self.check_element_visibility_and_wait(driver, logout_button)

        assert driver.current_url == acc_profile_page

        self.click_element(driver, logout_button)
        self.check_element_visibility_and_wait(driver, button_access)

        assert driver.current_url == auth_url

