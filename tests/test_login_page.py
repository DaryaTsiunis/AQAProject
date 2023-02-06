from pages.login_page import LoginPage
import allure


@allure.feature('Check login page')
@allure.story('Check login with correct data')
def test_check_login_with_correct_data(driver):
    with allure.step('Open Login page'):
        login_page = LoginPage(driver)
        login_page.open()
    with allure.step('Enter login'):
        login_page.enter_login_name()
    with allure.step('Enter password'):
        login_page.enter_password()
    with allure.step('Press submit button'):
        login_page.press_submit_button()
    assert login_page.page_url != login_page.present_url()


@allure.feature('Check login page')
@allure.story('Check login with incorrect login')
def test_check_login_with_incorrect_login(driver):
    with allure.step('Open Login page'):
        login_page = LoginPage(driver)
        login_page.open()
    with allure.step('Enter incorrect login'):
        login_page.enter_incorrect_login_name()
    with allure.step('Enter password'):
        login_page.enter_password()
    with allure.step('Press submit button'):
        login_page.press_submit_button()
    with allure.step('Check alert message'):
        assert login_page.alert_message_text() == f'Пользователя с таким логином ' \
                                                  f'({login_page.incorrect_login_text}) не существует'


@allure.feature('Check login page')
@allure.story('Check login with incorrect password')
def test_check_login_with_incorrect_password(driver):
    with allure.step('Open Login page'):
        login_page = LoginPage(driver)
        login_page.open()
    with allure.step('Enter login'):
        login_page.enter_login_name()
    with allure.step('Enter incorrect password'):
        login_page.enter_incorrect_password()
    with allure.step('Press submit button'):
        login_page.press_submit_button()
    with allure.step('Check alert message'):
        assert login_page.alert_message_text() == 'Неправильный пароль'


@allure.feature('Check login page')
@allure.story('Check login blank fields')
def test_check_login_with_blank_fields(driver):
    with allure.step('Open Login page'):
        login_page = LoginPage(driver)
        login_page.open()
    with allure.step('Press submit button'):
        login_page.press_submit_button()
    with allure.step('Check alert message'):
        assert login_page.alert_message_text() == 'Не задан логин'


@allure.feature('Check login page')
@allure.story('Check mask password')
def test_check_password_is_masked(driver):
    with allure.step('Open Login page'):
        login_page = LoginPage(driver)
        login_page.open()
    with allure.step('Check password is masked'):
        assert login_page.password_mask_check() == 'password'
