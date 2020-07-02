from selenium.webdriver.common.by import By
from Configurations.read_json import driver_conf
from Libs.UiHelpers import UiHelpers
class LoginPage:

    def __init__(self):
        self.url = UiHelpers.get_url(driver_conf.url)
        self.user_name_txt = (By.NAME, 'userName')
        self.user_password_txt = (By.NAME,'password')
        self.login_btn = (By.NAME,'login')

    def input_user_name(self, username):
        UiHelpers.send_keys(self.user_name_txt, username)

    def input_user_password(self, password):
        UiHelpers.send_keys(self.user_name_txt, password)

    def click_on_login(self):
        UiHelpers.click_element(self.login_btn)


