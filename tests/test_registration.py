import random
from time import sleep
from base_class import BaseClass
from reg_page_elements import element_name, element_email, element_password, button_registration, element_error


class TestRegistration(BaseClass):

    def test_register_correct_value_positive_case(self, driver):
        names = ['Lika', 'Ivan', 'Petr', 'Roman']
        driver.get("https://stellarburgers.nomoreparties.site/register")
        name = names[random.randint(0, len(names) - 1)]
        email = f"{name}{random.randint(0, 10000)}@mail.ru"
        self.send_keys(driver, element_name, name)
        self.send_keys(driver, element_email, email)
        self.send_keys(driver, element_password, "parol123")
        self.click_element(driver, button_registration)
        sleep(0.5)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    def test_register_incorrect_password_negative_case(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        self.send_keys(driver, element_name, "Lika")
        self.send_keys(driver, element_email, "lika.proskurina23@mail.ru")
        self.send_keys(driver, element_password, "par")
        self.click_element(driver, button_registration)
        error = self.get_element_text(driver, element_error)
        assert error == 'Некорректный пароль'
        driver.quit()
