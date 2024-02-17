
Feature: Login Feature

Scenario Outline: Successful Login
    Given I am on the login page
    When I enter username "my_username" and password "my_password"
    And I click the login button
    Then I should be logged in

    Examples: Testdata
        | my_username           | my_password   |
        | nsc+iosdev@mega.co.nz | Small2000     |