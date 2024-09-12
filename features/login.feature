Feature: Login Functionality

  Background:
    Given the user is on the login page

  @happy_path
  Scenario: Successful login with valid credentials
    When the user logs in with valid credentials
    Then the system shows the home page

  @exception
  Scenario Outline:
    When the user logs in with <user> and <password>
    Then the system shows an error

    Examples:
      | user | password |
      | stu  | 123Pass  |