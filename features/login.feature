Feature: As an user I am able to login in swaglabs system

  Scenario Template: log into the swaglabs system
    Given user enters his <username> and <password> in the login page
    When  click the "Login" button
    Then  the homepage of the online store is displayed

    Examples: First user
      | username         | password     |
      | standard_user    | secret_sauce |
      | locked_out_user  | secret_sauce |
      | problem_user     | secret_sauce |


