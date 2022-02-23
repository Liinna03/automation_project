import time

from behave import *

from pages.cart.cart_page import ShoppingCartPage
from pages.checkout_information.checkout_information_page import CheckoutInformationPage
from pages.locators.locators import ProductsPageLocator
from pages.products.products_page import ChooseProducts
from pages.checkout_overview_page.checkout_overview_page import CheckOverviewPage
from wrappers.time.is_present import is_element_present


@given('the user adds two products to the shopping cart')
def step_impl(context):
    choose_product = ChooseProducts(context.driver)
    choose_product.select_first_product()
    is_element_present(context.driver, *ProductsPageLocator.add_second_product)
    choose_product.select_second_product()


@when('go at shopping cart')
def step_impl(context):
    click_shopping_cart = ChooseProducts(context.driver)
    click_shopping_cart.select_shopping_cart()
    is_element_present(context.driver, *ProductsPageLocator.shopping_cart)


@then('the two products will be in the shopping cart')
def step_impl(context):
    finish = ShoppingCartPage(context.driver)
    assert finish.confirm_products_in_the_cart()
