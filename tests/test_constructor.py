from data.test_data import auth_email, password
from locators import auth_page_elements as auth_elements
from base_class import BaseClass
from locators.home_page_elements import button_personal_account, constructor_button, element_make_burger, logo_element, \
    sauce_section_element, bun_section_element, text_bun_section, text_sauce_section, text_stuffing_section, \
    stuffing_section_element
from locators.private_account_page_elements import logout_button
from urls.site_urls import auth_url, home_page_url, acc_profile_page


class TestConstructor(BaseClass):

    def test_constructor_button_access(self, driver):
        driver.get(auth_url)
        self.send_keys(driver, auth_elements.element_email, auth_email)
        self.send_keys(driver, auth_elements.element_password, password)
        self.click_element(driver, auth_elements.button_access)
        self.check_element_visibility_and_wait(driver, bun_section_element)

        assert driver.current_url == home_page_url

        self.click_element(driver, button_personal_account)
        self.check_element_visibility_and_wait(driver, logout_button)

        assert driver.current_url == acc_profile_page

        self.click_element(driver, constructor_button)

        assert driver.current_url == home_page_url
        assert self.get_element_text(driver, element_make_burger) == 'Соберите бургер'


    def test_constructor_logo_access(self, driver):
        driver.get(auth_url)
        self.send_keys(driver, auth_elements.element_email, auth_email)
        self.send_keys(driver, auth_elements.element_password, password)
        self.click_element(driver, auth_elements.button_access)
        self.check_element_visibility_and_wait(driver, bun_section_element)

        assert driver.current_url == home_page_url

        self.click_element(driver, button_personal_account)
        self.check_element_visibility_and_wait(driver, logout_button)

        assert driver.current_url == acc_profile_page

        self.click_element(driver, logo_element)

        assert driver.current_url == home_page_url
        assert self.get_element_text(driver, element_make_burger) == 'Соберите бургер'


    def test_bun_section_access(self, driver):

        driver.get(home_page_url)
        self.click_element(driver, sauce_section_element)
        self.click_element(driver, bun_section_element)

        assert self.is_element_displayed(driver, text_bun_section)

    def test_sauce_section_access(self, driver):

        driver.get(home_page_url)
        self.click_element(driver, sauce_section_element)

        assert self.is_element_displayed(driver, text_sauce_section)

    def test_stuffing_section_access(self, driver):

        driver.get(home_page_url)
        self.click_element(driver, stuffing_section_element)

        assert self.is_element_displayed(driver, text_stuffing_section)

