from pages.base_page import BasePage
from locators import loc_home_page as loc


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://tvoydnevnik.com'

    def bell_button_click(self):
        bell_button = self.find(loc.bell_button)
        bell_button.click()

    def notifications_is_displayed(self):
        notifications = self.find(loc.my_notifications)
        return notifications.is_displayed()

    def messages_button_click(self):
        messages_button = self.find(loc.messages_button)
        messages_button.click()

    def my_messages_is_displayed(self):
        my_messages = self.find(loc.my_messages)
        return my_messages.is_displayed()

    def new_message_button_click(self):
        new_message_button = self.find(loc.new_message_button)
        new_message_button.click()

    def my_new_message_is_displayed(self):
        my_new_message = self.find(loc.my_new_message)
        return my_new_message.is_displayed()

    def settings_button_click(self):
        settings_button = self.find(loc.settings_button)
        settings_button.click()

    def settings_is_displayed(self):
        settings = self.find(loc.my_settings_text)
        return settings.is_displayed()

    def contacts_button_click(self):
        contacts_button = self.find(loc.contacts_button)
        contacts_button.click()

    def contacts_is_displayed(self):
        contacts = self.find(loc.contacts)
        return contacts.is_displayed()

    def help_and_support_button_click(self):
        help_and_support_button = self.find(loc.help_and_support_button)
        help_and_support_button.click()

    def help_and_support_is_displayed(self):
        help_and_support = self.find(loc.help_and_support)
        return help_and_support.is_displayed()

    def side_menu_button_click(self):
        side_menu_button = self.find(loc.side_menu_button)
        side_menu_button.click()

    def side_menu_is_displayed(self):
        side_menu = self.find(loc.side_menu)
        return side_menu.is_displayed()

    def google_store_button_click(self):
        google_store_button = self.find(loc.google_store_button)
        google_store_button.click()

    def google_store_product_name(self):
        google_store_product = self.find(loc.google_store_product)
        return google_store_product.text

    def apple_store_button_click(self):
        apple_store_button = self.find(loc.apple_store_button)
        apple_store_button.click()

    def apple_store_product_name(self):
        apple_store_product = self.find(loc.apple_store_product)
        return apple_store_product.text
