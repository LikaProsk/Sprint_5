from base_class import BaseClass
from data.test_data import password, auth_login, auth_email, incorrect_password
from locators.auth_page_elements import button_access
from locators.reg_page_elements import element_name, element_email, element_password, button_registration, element_error
from urls.site_urls import reg_page_url, auth_url


class TestRegistration(BaseClass):

    def test_register_correct_value_positive_case(self, driver, reg_name, reg_email):
        driver.get(reg_page_url)

        self.send_keys(driver, element_name, reg_name)
        self.send_keys(driver, element_email, reg_email)
        self.send_keys(driver, element_password, password)
        self.click_element(driver, button_registration)
        self.check_element_visibility_and_wait(driver, button_access, 30)

        assert driver.current_url == auth_url


    def test_register_incorrect_password_negative_case(self, driver):
        driver.get(reg_page_url)
        self.send_keys(driver, element_name, auth_login)
        self.send_keys(driver, element_email, auth_email)
        self.send_keys(driver, element_password, incorrect_password)
        self.click_element(driver, button_registration)
        error = self.get_element_text(driver, element_error)
        assert error == 'Некорректный пароль'

