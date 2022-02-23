from selenium.webdriver.common.by import By


class LoginPageLocator(object):
    txt_username_field = (By.ID, 'user-name')
    txt_password_field = (By.ID, 'password')
    btn_login = (By.ID, 'login-button')
    logo_home_page = (By.CSS_SELECTOR, '#header_container > div.primary_header > div.header_label > div')


class ProductsPageLocator(object):
    add_first_product = (By.ID, 'add-to-cart-sauce-labs-backpack')
    add_second_product = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    shopping_cart = (By.CSS_SELECTOR, '.shopping_cart_link')


class ShoppingCartLocator(object):
    btn_checkout = (By.ID, 'checkout')
    title_first_product = (By.CSS_SELECTOR, '.cart_list > div:nth-of-type(3) .inventory_item_name')
    title_second_product = (By.CSS_SELECTOR, 'div:nth-of-type(4) .inventory_item_name')


class CheckoutInformationLocator(object):
    txt_first_name = (By.ID, 'first-name')
    txt_last_name = (By.ID, 'last-name')
    txt_postal_code = (By.ID, 'postal-code')
    btn_continue = (By.ID, 'continue')


class CheckoutOverviewLocator(object):
    btn_finish = (By.ID, 'finish')
    created_succe = (By.CSS_SELECTOR, '#header_container > div.header_secondary_container > span')
