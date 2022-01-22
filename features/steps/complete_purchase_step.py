import time


from behave import *
from pages.cart.cart_page import ShoppingCartPage
from pages.checkout_information.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview_page.checkout_overview_page import CheckOverviewPage


@given('user has products in the cart and clicks on the checkout button')
def step_impl(context):
    click_checkout_btn = ShoppingCartPage(context.driver)
    click_checkout_btn.click_checkout()
    time.sleep(5)


@When('user completes checkout information with her {first_name}, {last_name} and {postal_code}')
def step_impl(context, first_name, last_name, postal_code):
    complete_form = CheckoutInformationPage(context.driver)
    complete_form.enter_first_name(first_name)
    complete_form.enter_last_name(last_name)
    complete_form.enter_postal_code(postal_code)


@when('click on the continue button in the CHECKOUT page')
def step_impl(context):
    continue_button = CheckoutInformationPage(context.driver)
    continue_button.click_btn_continue()


@when('click on the finish button in the CHECKOUT: OVERVIEW page')
def step_impl(context):
    finish_button = CheckOverviewPage(context.driver)
    finish_button.click_finish_btn()


@Then('the purchase is completed successfully')
def step_impl(context):
    purchase_complete = CheckOverviewPage(context.driver)
    assert purchase_complete.created_successfully()

