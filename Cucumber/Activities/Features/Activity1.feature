@activity1
Feature: Basic Syntax
  @Scenario1
  Scenario: Opening a Webpage using Selenium
    Given User is on Google Home Page
    When User types in Cheese and hits ENTER
    Then Show how many search results were shown
    And Close the browser
