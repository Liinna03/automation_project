Feature: As an user I am able to buy products in the online store swaglabs

  Background:
    Given user enters his username and password in the login_page
    When  click the "Login" button
    Then  online store homepage is displayed

  Scenario: add products in the shopping cart
    Given the user adds two products to the shopping cart
    When  go at shopping cart
    Then  the two products will be in the shopping cart
