import random

import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture()
def reg_name():
    names = ['Lika', 'Ivan', 'Petr', 'Roman']
    return names[random.randint(0, len(names) - 1)]

@pytest.fixture()
def reg_email():
    return f"user{random.randint(0, 10000)}@mail.ru"