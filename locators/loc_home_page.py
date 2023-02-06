from selenium.webdriver.common.by import By


bell_button = (By.CSS_SELECTOR, 'svg[name="bell"]')
my_notifications = (By.CSS_SELECTOR, 'div[class=" mzr-font--body14sb"]')

messages_button = (By.CSS_SELECTOR, 'svg[name="message"]')
my_messages = (By.XPATH, '//div[text()="Диалоги"]')

new_message_button = (By.CSS_SELECTOR, 'svg[name="editDoc"]')
my_new_message = (By.XPATH, '//div[text()="Новое сообщение"]')

settings_button = (By.CSS_SELECTOR, 'svg[name="settings"]')
my_settings_text = (By.XPATH, '//div[text()="Настройки"]')

contacts_button = (By.LINK_TEXT, 'КОНТАКТЫ')
contacts = (By.CSS_SELECTOR, 'div[class="mzr-block-header "]')

help_and_support_button = (By.XPATH, '//a[text()="Помощь и обратная связь"]')
help_and_support = (By.XPATH, '//div[text()="Справка"]')

side_menu_button = (By.XPATH, '//div[text()="Общая лента"]')
side_menu = (By.CSS_SELECTOR, 'div[class="mzr-top-menu-header"]')

google_store_button = (By.CSS_SELECTOR, 'a[title="Приложение для android"]')
google_store_product = (By.XPATH, '//h1[@class="Fd93Bb ynrBgc xwcR9d"]')

apple_store_button = (By.CSS_SELECTOR, 'a[title="Приложение для apple"]')
apple_store_product = (By.XPATH, '//h1[@class="product-header__title app-header__title"]')
