from selenium.webdriver.common.by import By

element_name = (By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input") # Поле ввода имени
element_email = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input") # Поле ввода пароля
element_password = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input") # Поле ввода пароля
button_registration = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]") # Кнопка "Зарегистироваться"
element_error = (By.XPATH, "//p[@class='input__error text_type_main-default']") # Ошибка "Некорректный пароль"

