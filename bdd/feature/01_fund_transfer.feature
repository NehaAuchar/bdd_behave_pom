# Created by nehaauchar at 08/10/2024
Feature: Fund Transfer
#  As a customer , user wants to transfer funds from one account to another.

  Background:  Application login
    Given user has valid credentials to login

  @valid @smoke @positive @regression
  Scenario Outline: Valid : Fund transfer with valid details
    When user clicks on Transfer Funds
    When user selects the "<FromAccount>" as "From" account
    And user selects the "<ToAccount>" as "To" account
    And user enters the amount to be transferred as "<Amount>"
    And user clicks on confirmation button
    Then user should see the error message as "<Message>"
    And user clicks on Account Overview to check account balance
    And the checking account balance should be "<FromBalance>" for "<FromAccount>"
    And the savings account balance should "<ToBalance>" for "<ToAccount>"
    Examples:
      | FromAccount | ToAccount | Amount | Message           | FromBalance | ToBalance |
      | 14787       | 16008     | 100    | Transfer Complete | $115.50     | $400.00   |
      | 16008       | 14787     | 100    | Transfer Complete | $300.00     | $215.50   |


  Scenario Outline: Valid : Fund transfer with invalid details
    When user clicks on Transfer Funds
    When user selects the "<FromAccount>" as "From" account
    And user selects the "<ToAccount>" as "To" account
    And user enters the amount to be transferred as "<Amount>"
    And user clicks on confirmation button
    Then user should see the error message as "<Message>"
    And user clicks on Account Overview to check account balance
    And the checking account balance should be "<FromBalance>" for "<FromAccount>"
    And the savings account balance should "<ToBalance>" for "<ToAccount>"
    Examples:
      | FromAccount | ToAccount | Amount | Message                     | FromBalance     | ToBalance       |
      | 14787       | 16008     | 0      | "Invalid amount entered"    | remain the same | remain the same |
      | 14787       | 16008     | 1000   | "Insufficient funds"        | remain the same | remain the same |
      | 14787       | 14787     | 100    | "Invalid account selection" | remain the same | remain the same |
      | 14787       | 16008     | 100    | "Account blocked or closed" | remain the same | remain the same |