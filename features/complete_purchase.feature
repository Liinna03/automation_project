Feature: As an user I am able to buy products in the online store swaglabs

  Background:
    Given user enters his username and password in the login_page
    When  click the "Login" button
    Then  online store homepage is displayed
    Given the user adds two products to the shopping cart
    When  go at shopping cart
    Then  the two products will be in the shopping cart

  Scenario Outline: complete purchase and information checkout
    Given user has products in the cart and clicks on the checkout button
    When  user completes checkout information with her <first_name>, <last_name> and <postal_code>
    And   click on the continue button in the CHECKOUT page
    And   click on the finish button in the CHECKOUT: OVERVIEW page
    Then  the purchase is completed successfully

    Examples:
      | first_name | last_name | postal_code |
      | Juan       | Gomez     | 756         |
