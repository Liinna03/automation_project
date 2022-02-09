import time

from selenium.common.exceptions import NoSuchElementException

from pages.base import BasePage
from pages.locators.locators import LoginPageLocator


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

    def created_successfully(self):
        return True if self.driver.find_element(*LoginPageLocator.logo_home_page) else False
""""
        try:
            element = self.driver.find_element(*LoginPageLocator.logo_home_page)
            return True
        except NoSuchElementException as e:
            return False
        time.sleep(10)
"""