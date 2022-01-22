from pages.base import BasePage
from pages.locators.locators import ShoppingCartLocator


class ShoppingCartPage(BasePage):
    def click_checkout(self):
        element = self.driver.find_element(*ShoppingCartLocator.btn_checkout)
        element.click()

    def confirm_products_in_the_cart(self):
        element = self.driver.find_element(*ShoppingCartLocator.title_first_product).text
        element1 = self.driver.find_element(*ShoppingCartLocator.title_second_product).text
        return True if element == "Sauce Labs Backpack" and element1 == "Sauce Labs Bike Light" else False
