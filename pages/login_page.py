from pages.base_page import BasePage
from locators import loc_login_page as loc
import constants as con


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://tvoydnevnik.com/account/login'

    def enter_login_name(self):
        login = self.find(loc.login_field)
        login.send_keys(con.correct_login)

    def enter_incorrect_login_name(self):
        login = self.find(loc.login_field)
        login.send_keys(con.incorrect_login)

    def enter_password(self):
        password = self.find(loc.password_field)
        password.send_keys(con.password)

    def enter_incorrect_password(self):
        password = self.find(loc.password_field)
        password.send_keys(con.incorrect_password)

    def press_submit_button(self):
        submit = self.find(loc.submit_button)
        submit.click()

    def alert_message_text(self):
        alert_text = self.find(loc.alert_message)
        return alert_text.text

    def click_captcha(self):
        captcha_checkbox = self.find(loc.captcha)
        return captcha_checkbox.click()

    def password_mask_check(self):
        password = self.find(loc.password_field)
        return password.get_attribute('type')
