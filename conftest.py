from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('user-data-dir=C:/Users/user-data')
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()
