from pages.home_page import HomePage
import allure


@allure.feature('Check home page')
@allure.story('Check home page is open')
def test_home_page(driver):
    with allure.step('Open Home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Home page is open'):
        assert home_page.present_url() == 'https://tvoydnevnik.com/'


@allure.feature('Check home page')
@allure.story('Check bell button')
def test_bell_button(driver):
    with allure.step('Open Home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Click bell button'):
        home_page.bell_button_click()
    with allure.step('Notifications is displayed'):
        assert home_page.notifications_is_displayed()


@allure.feature('Check home page')
@allure.story('Check messages button')
def test_messages_button(driver):
    with allure.step('Open Home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Click messages button'):
        home_page.messages_button_click()
    with allure.step('My messages is displayed'):
        assert home_page.my_messages_is_displayed()


@allure.feature('Check home page')
@allure.story('Check new message button')
def test_new_message_button(driver):
    with allure.step('Open Home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Click new message button'):
        home_page.new_message_button_click()
    with allure.step('My new message is displayed'):
        assert home_page.my_new_message_is_displayed()


@allure.feature('Check home page')
@allure.story('Check settings button')
def test_setting_button(driver):
    with allure.step('Open Home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Click settings button'):
        home_page.settings_button_click()
    with allure.step('Settings is displayed'):
        assert home_page.settings_is_displayed()


@allure.feature('Check home page')
@allure.story('Check contacts button')
def test_contacts_button(driver):
    with allure.step('Open Home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Scroll to bottom'):
        home_page.scroll_down()
    with allure.step('Click contacts button'):
        home_page.contacts_button_click()
    with allure.step('Contacts is displayed'):
        assert home_page.contacts_is_displayed()


@allure.feature('Check home page')
@allure.story('Check help and support button')
def test_help_and_support_button(driver):
    with allure.step('Open Home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Click help and support button'):
        home_page.help_and_support_button_click()
    with allure.step('Help and support is displayed'):
        assert home_page.help_and_support_is_displayed()


@allure.feature('Check home page')
@allure.story('Check side menu button')
def test_side_menu_button(driver):
    with allure.step('Open Home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Click side menu button'):
        home_page.side_menu_button_click()
    with allure.step('Side menu is displayed'):
        assert home_page.side_menu_is_displayed()


@allure.feature('Check home page')
@allure.story('Check google store button')
def test_google_store_button(driver):
    with allure.step('Open Home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Click google store button'):
        home_page.google_store_button_click()
    with allure.step('Switch to tab'):
        home_page.switch_to_window()
    with allure.step('Product in google store is displayed'):
        assert home_page.google_store_product_name() == 'Дневник Зожника'


@allure.feature('Check home page')
@allure.story('Check apple store button')
def test_apple_store_button(driver):
    with allure.step('Open Home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Click apple store button'):
        home_page.apple_store_button_click()
    with allure.step('Switch to tab'):
        home_page.switch_to_window()
    with allure.step('Product in apple store is displayed'):
        assert home_page.apple_store_product_name() == 'Дневник зожника 9+'
