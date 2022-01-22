import time

from behave import *

from pages.cart.cart_page import ShoppingCartPage
from pages.checkout_information.checkout_information_page import CheckoutInformationPage
from pages.products.products_page import ChooseProducts
from pages.checkout_overview_page.checkout_overview_page import CheckOverviewPage


@given('the user adds two products to the shopping cart')
def step_impl(context):
    choose_product = ChooseProducts(context.driver)
    choose_product.select_first_product()
    time.sleep(5)
    choose_product.select_second_product()
    time.sleep(5)


@when('go at shopping cart')
def step_impl(context):
    click_shopping_cart = ChooseProducts(context.driver)
    click_shopping_cart.select_shopping_cart()
    time.sleep(5)


@then('the two products will be in the shopping cart')
def step_impl(context):
    finish = ShoppingCartPage(context.driver)
    assert finish.confirm_products_in_the_cart()
