from pages.base_page import BasePage
from locators import loc_settings_page as loc
from selenium.webdriver.common.keys import Keys
import constants as con


class SettingsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://tvoydnevnik.com/people/user/20139564/edit'

    def open_my_account(self):
        my_account_button = self.find(loc.my_account_button)
        my_account_button.click()

    def enter_name(self):
        name_field = self.find_all(loc.name_field)
        name_field[0].click()
        for i in range(51):
            name_field[0].send_keys(Keys.BACKSPACE)
        name_field[0].send_keys(con.name)
        return con.name

    def save_button_click(self):
        save_button = self.find(loc.save_button)
        save_button.click()

    def get_name_field_attr(self):
        name_field = self.find_all(loc.name_field)
        return name_field[0].get_attribute('value')

    def clear_name_field(self):
        name_field = self.find_all(loc.name_field)
        name_field[0].click()
        for i in range(51):
            name_field[0].send_keys(Keys.BACKSPACE)

    def name_alert_is_displayed(self):
        name_alert = self.find(loc.name_alert)
        return name_alert.is_displayed()

    def enter_about_me(self):
        about_me_field = self.find(loc.about_me_field)
        about_me_field.click()
        for i in range(151):
            about_me_field.send_keys(Keys.BACKSPACE)
        about_me_field.send_keys(con.about_me)
        return con.about_me

    def get_about_me_field_text(self):
        about_me_field = self.find(loc.about_me_field)
        return about_me_field.text

    def enter_site(self):
        site_field = self.find_all(loc.site_field)
        site_field[1].click()
        for i in range(51):
            site_field[1].send_keys(Keys.BACKSPACE)
        site_field[1].send_keys(con.site)
        return con.site

    def get_site_field_attr(self):
        site_field = self.find_all(loc.site_field)
        return site_field[1].get_attribute('value')

    def theme_button_click(self):
        theme_button = self.find(loc.theme_button)
        theme_button.click()

    def choose_theme_button_click(self):
        red_theme_button = self.find(loc.red_theme_button)
        red_theme_button.click()

    def get_main_theme(self):
        main_theme = self.find(loc.main_theme)
        return main_theme.get_attribute('data-theme')

    def choose_text_theme_button_click(self):
        arial_text_theme = self.find(loc.arial_text_theme_button)
        arial_text_theme.click()

    def get_main_text_theme(self):
        main_text_theme = self.find(loc.main_text_theme)
        return main_text_theme.get_attribute('data-font')

    def log_out_button_click(self):
        log_out_button = self.find(loc.log_out_button)
        log_out_button.click()

    def login_button_is_displayed(self):
        login_button = self.find(loc.login_button)
        return login_button.is_displayed()

    def personal_data_button_click(self):
        personal_data_button = self.find(loc.personal_data)
        personal_data_button.click()

    def height_text(self):
        height = self.find_all(loc.height_field)
        height[0].click()
        height[0].send_keys(Keys.BACKSPACE)
        height[0].send_keys(con.height_text)
        return con.height_text

    def get_height_attr(self):
        height = self.find_all(loc.height_field)
        return height[0].get_attribute('value')

    def weight_text(self):
        weight = self.find_all(loc.weight_field)
        weight[1].click()
        weight[1].send_keys(Keys.BACKSPACE)
        weight[1].send_keys(con.weight_text)
        return con.weight_text

    def get_weight_attr(self):
        weight = self.find_all(loc.weight_field)
        return weight[1].get_attribute('value')
