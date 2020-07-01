import polling
from selenium.webdriver.common.by import By
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
    def send_keys(cls, locator, input):
        cls.find_element(locator).send_keys(input)





