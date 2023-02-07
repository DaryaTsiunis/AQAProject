from selenium.webdriver.common.by import By


my_account_button = (By.XPATH, '//div[text()="Мой профиль"]')
name_field = (By.XPATH, '//div[@class="uk-form-controls "]/input')
save_button = (By.XPATH, '//button[@class="uk-button uk-button-primary "]')
name_alert = (By.XPATH, '//div[text()="Неправильное имя пользователя: длина должна быть больше 2"]')
about_me_field = (By.XPATH, '//div[@class="uk-form-controls "]/textarea')
site_field = (By.XPATH, '//div[@class="uk-form-controls "]/input')
theme_button = (By.XPATH, '//div[text()="Тема оформления"]')
red_theme_button = (By.XPATH, '//button[text()="Красная"]')
arial_text_theme_button = (By.XPATH, '//button[text()="Arial"]')
main_theme = (By.TAG_NAME, 'html')
main_text_theme = (By.TAG_NAME, 'html')
log_out_button = (By.XPATH, '//div[text()="Выйти"]')
login_button = (By.XPATH, '//a[text()="Войти"]')
personal_data = (By.XPATH, '//div[text()="Настройки норм питания"]')
height_field = (By.XPATH, '//div[@class="uk-flex uk-position-relative"]/input')
weight_field = (By.XPATH, '//div[@class="uk-flex uk-position-relative"]/input')
