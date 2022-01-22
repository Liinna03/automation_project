from pages.base import BasePage
from pages.locators.locators import CheckoutOverviewLocator


class CheckOverviewPage(BasePage):
    def click_finish_btn(self):
        element = self.driver.find_element(*CheckoutOverviewLocator.btn_finish)
        element.click()

    def created_successfully(self):
        element = self.driver.find_element(*CheckoutOverviewLocator.created_succe).text
        return True if element == "CHECKOUT: COMPLETE!" else False

