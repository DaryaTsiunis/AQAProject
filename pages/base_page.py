from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.page_url = ''

    def open(self):
        if self.page_url:
            self.driver.get(self.page_url)
        else:
            raise NotImplementedError

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def scroll_down(self):
        return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def present_url(self):
        return self.driver.current_url

    def switch_to_window(self):
        tabs = self.driver.window_handles
        return self.driver.switch_to.window(tabs[1])

    def refresh_page(self):
        return self.driver.refresh()
