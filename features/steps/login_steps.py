import time
import json

from behave import *
from pages.login.login_page import *

with open("test_data/data.json") as conf:
    data = json.load(conf)


@given(u'user enters his {username} and {password} in the login page')
def step_impl(context, username, password):
    login = Login(context.driver)
    login.enter_username(username)
    login.enter_password(password)


@given(u'user enters his username and password in the login_page')
def step_impl(context):
    login_page = Login(context.driver)
    time.sleep(3)
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])


@When('click the "Login" button')
def step_impl(context):
    login_button = Login(context.driver)
    login_button.click_login_button()


@Then('the homepage of the online store is displayed')
def step_impl(context):
    confirmation = Login(context.driver)
    confirmation.created_successfully()
    time.sleep(10)

