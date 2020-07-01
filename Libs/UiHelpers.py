import polling
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Libs.WebDriverManager import WebDriverManager

class UiHelpers:
    _driver = WebDriverManager.get_browser()

    @classmethod
    def get_url(cls, url):
        cls._driver.get(url)

    @classmethod
    def find_element(cls, locator):
        try:
            elem = polling.poll(
                lambda: cls._driver.find_element(*locator),
                        step=0.5,
                        timeout=7)
            return elem
        except Exception as e:
            raise Exception("Finding locator failed -{} to find locator - {}. ".format(locator, e))

    @classmethod
    def find_elements(cls, locator):
        try:
            elem = polling.poll(
                lambda: cls._driver.find_elements(*locator),
                step=0.5,
                timeout=7)
            return elem
        except Exception as e:
            raise Exception("Finding locator failed -{} to find locator - {}. ".format(locator, e))

    @classmethod
    def send_keys(cls, locator, input):
        cls.find_element(locator).send_keys(input)

    @classmethod
    def select_dropdown_by_index(cls, locator, idx):
        s = Select(cls.find_element(locator))
        s.select_by_index(idx)

    @classmethod
    def select_dropdown_by_value(cls, locator, value):
        s = Select(cls.find_element(locator))
        s.select_by_value(value)

    @classmethod
    def select_dropdown_by_text(cls, locator, text):
        s = Select(cls.find_element(locator))
        s.select_by_visible_text(text)

    @classmethod
    def quit_browser(cls):
        cls._driver.quit()

    @classmethod
    def close_window(cls):
        cls._driver.close()
