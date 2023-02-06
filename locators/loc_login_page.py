from selenium.webdriver.common.by import By


login_field = (By.ID, 'login')
password_field = (By.ID, 'password')
submit_button = (By.XPATH, '//button[@value="login"]')
alert_message = (By.XPATH, '//div[@class="uk-alert uk-alert-danger"]')
captcha = (By.XPATH, '//div[@class="recaptcha-checkbox-border"]')
