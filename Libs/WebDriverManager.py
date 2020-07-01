from selenium import webdriver
from Configurations.read_json import driver_conf

class WebDriverManager:
    driver = None
    wait = None

    @classmethod
    def get_browser(cls):
        if not cls.driver:
            support_browsers = ["chrome", "firefox", "ie"]
            browser_name = driver_conf.browser_name.lower()
            if browser_name in support_browsers:
                if browser_name == "chrome":
                    cls.driver = webdriver.Chrome("")
                if browser_name == "firefox":
                    cls.driver = webdriver.Firefox(executable_path="/home/acme/selenium/SeleniumPython/seleniumdrivers/geckodriver")

                if browser_name == "ie":
                    cls.driver = webdriver.ie()

                cls.driver.maximize_window()
                cls.driver.delete_all_cookies()
                return cls.driver
            else:
                raise AttributeError("{} browser is not supported.".format(browser_name))


    @classmethod
    def close_browser(cls):
        if cls.driver:
            cls.driver.quit()


