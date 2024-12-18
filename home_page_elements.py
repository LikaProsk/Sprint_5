from selenium.webdriver.common.by import By


button_personal_account = (By.LINK_TEXT, "Личный Кабинет") # Кнопка "Личный Кабинет"
button_account_access = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]") # Кнопка "Войти в аккаунт"
element_make_burger = (By.XPATH, "//h1") # Заголовок "Соберите бургер"
constructor_button = (By.LINK_TEXT, "Конструктор") # Кнопка "Конструктор"
logo_element = ( By.XPATH, "//a[@href='/']") # Логотип "Stellar Burgers"
sauce_section_element = (By.XPATH, "//span[contains(text(), 'Соусы')]") # Раздел "Соусы"
bun_section_element = (By.XPATH, "//span[contains(text(), 'Булки')]") # Раздел "Булки"
stuffing_section_element = (By.XPATH, "//span[contains(text(), 'Начинки')]") # Раздел "Начинки"

