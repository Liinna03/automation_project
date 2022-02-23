from pages.base import BasePage
from pages.locators.locators import LoginPageLocator
from wrappers.time.is_present import is_element_present


class Login(BasePage):
    def enter_username(self, username):
        element = self.driver.find_element(*LoginPageLocator.txt_username_field)
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        element = self.driver.find_element(*LoginPageLocator.txt_password_field)
        element.clear()
        element.send_keys(password)

    def click_login_button(self):
        element = self.driver.find_element(*LoginPageLocator.btn_login)
        element.click()

    def login_successfully(self):
        return is_element_present(self.driver, *LoginPageLocator.logo_home_page)
