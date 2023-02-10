from pages.settings_page import SettingsPage
import allure
import pytest


@pytest.mark.order(26)
@allure.feature('Check settings page')
@allure.story('Check settings page is open')
def test_settings_page(driver):
    with allure.step('Open Settings page'):
        settings_page = SettingsPage(driver)
        settings_page.open()
    with allure.step('Settings page is open'):
        assert settings_page.present_url() == 'https://tvoydnevnik.com/people/user/20139564/edit'


@pytest.mark.order(27)
@allure.feature('Check settings page')
@allure.story('Check enter name field with blank')
def test_enter_name_field_with_blank(driver):
    with allure.step('Open Settings page'):
        settings_page = SettingsPage(driver)
        settings_page.open()
    with allure.step('Open my account'):
        settings_page.open_my_account()
    with allure.step('Clear name field'):
        settings_page.clear_name_field()
    with allure.step('Press save button'):
        settings_page.save_button_click()
    with allure.step('Name alert is displayed'):
        settings_page.name_alert_is_displayed()


@pytest.mark.order(28)
@allure.feature('Check settings page')
@allure.story('Check enter name field with data')
def test_enter_name_field_with_data(driver):
    with allure.step('Open Settings page'):
        settings_page = SettingsPage(driver)
        settings_page.open()
    with allure.step('Open my account'):
        settings_page.open_my_account()
    with allure.step('Enter name'):
        name_text = settings_page.enter_name()
    with allure.step('Press save button'):
        settings_page.save_button_click()
    with allure.step('Get name field value'):
        name_value = settings_page.get_name_field_attr()
    with allure.step('Check name correctness'):
        assert name_text == name_value


@pytest.mark.order(29)
@allure.feature('Check settings page')
@allure.story('Check about me field with data')
def test_about_me_field_with_data(driver):
    with allure.step('Open Settings page'):
        settings_page = SettingsPage(driver)
        settings_page.open()
    with allure.step('Open my account'):
        settings_page.open_my_account()
    with allure.step('Enter about me'):
        about_me = settings_page.enter_about_me()
    with allure.step('Press save button'):
        settings_page.save_button_click()
    with allure.step('Get about me text'):
        about_me_text = settings_page.get_about_me_field_text()
    with allure.step('Check about me correctness'):
        assert about_me == about_me_text


@pytest.mark.order(30)
@allure.feature('Check settings page')
@allure.story('Check site field with data')
def test_site_field_with_data(driver):
    with allure.step('Open Settings page'):
        settings_page = SettingsPage(driver)
        settings_page.open()
    with allure.step('Open my account'):
        settings_page.open_my_account()
    with allure.step('Enter site'):
        site_text = settings_page.enter_site()
    with allure.step('Press save button'):
        settings_page.save_button_click()
    with allure.step('Get site field value'):
        site_value = settings_page.get_site_field_attr()
    with allure.step('Check site correctness'):
        assert site_text == site_value


@pytest.mark.order(31)
@allure.feature('Check settings page')
@allure.story('Check main theme color')
def test_main_theme(driver):
    with allure.step('Open Settings page'):
        settings_page = SettingsPage(driver)
        settings_page.open()
    with allure.step('Open themes'):
        settings_page.theme_button_click()
    with allure.step('Choose red theme'):
        settings_page.choose_theme_button_click()
    with allure.step('Check theme is red'):
        assert settings_page.get_main_theme() == 'default'


@pytest.mark.order(32)
@allure.feature('Check settings page')
@allure.story('Check main text theme')
def test_text_main_theme(driver):
    with allure.step('Open Settings page'):
        settings_page = SettingsPage(driver)
        settings_page.open()
    with allure.step('Open themes'):
        settings_page.theme_button_click()
    with allure.step('Choose arial text theme'):
        settings_page.choose_text_theme_button_click()
    with allure.step('Check text theme is arial'):
        assert settings_page.get_main_text_theme() == 'Arial'


@pytest.mark.order(33)
@allure.feature('Check settings page')
@allure.story('Check height data')
def test_height_data(driver):
    with allure.step('Open Settings page'):
        settings_page = SettingsPage(driver)
        settings_page.open()
    with allure.step('Press personal data'):
        settings_page.personal_data_button_click()
    with allure.step('Enter height'):
        height_text = settings_page.height_text()
    with allure.step('Get height value'):
        height_value = settings_page.get_height_attr()
    with allure.step('Check height correctness'):
        assert height_text == height_value


@pytest.mark.order(34)
@allure.feature('Check settings page')
@allure.story('Check weight data')
def test_weight_data(driver):
    with allure.step('Open Settings page'):
        settings_page = SettingsPage(driver)
        settings_page.open()
    with allure.step('Press personal data'):
        settings_page.personal_data_button_click()
    with allure.step('Enter weight'):
        weight_text = settings_page.weight_text()
    with allure.step('Get weight value'):
        weight_value = settings_page.get_weight_attr()
    with allure.step('Check weight correctness'):
        assert weight_text == weight_value


@pytest.mark.order(35)
@allure.feature('Check settings page')
@allure.story('Check logout button')
def test_logout_button(driver):
    with allure.step('Open Settings page'):
        settings_page = SettingsPage(driver)
        settings_page.open()
    with allure.step('Press logout button'):
        settings_page.log_out_button_click()
    with allure.step('Check logout success'):
        assert settings_page.login_button_is_displayed()
