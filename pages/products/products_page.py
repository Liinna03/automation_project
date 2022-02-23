from selenium.common.exceptions import NoSuchElementException

from pages.base import BasePage
from pages.locators.locators import ProductsPageLocator


class ChooseProducts(BasePage):
    def select_first_product(self):
        try:
            element = self.driver.find_element(*ProductsPageLocator.add_first_product)
            element.click()
        except NoSuchElementException as e:
            print("ERROR", e.__dict__["msg"])

    def select_second_product(self):
        try:
            element = self.driver.find_element(*ProductsPageLocator.add_second_product)
            element.click()
        except NoSuchElementException as e:
            print("ERROR", e.__dict__["msg"])

    def select_shopping_cart(self):
        element = self.driver.find_element(*ProductsPageLocator.shopping_cart)
        element.click()
