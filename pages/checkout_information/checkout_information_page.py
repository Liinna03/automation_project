from pages.base import BasePage
from pages.locators.locators import CheckoutInformationLocator


class CheckoutInformationPage(BasePage):
    def enter_first_name(self, first_name):
        element = self.driver.find_element(*CheckoutInformationLocator.txt_first_name)
        element.send_keys(first_name)

    def enter_last_name(self, last_name):
        element = self.driver.find_element(*CheckoutInformationLocator.txt_last_name)
        element.send_keys(last_name)

    def enter_postal_code(self, postal_code):
        element = self.driver.find_element(*CheckoutInformationLocator.txt_postal_code)
        element.send_keys(postal_code)

    def click_btn_continue(self):
        element = self.driver.find_element(*CheckoutInformationLocator.btn_continue)
        element.click()
