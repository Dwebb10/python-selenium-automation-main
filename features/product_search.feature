Feature: Test Scenarios for Search functionality


  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <product>
    Then Verify search results are shown for <product>
    Examples:
    |product  |
    |iphone   |
    |coffee   |
    |tea      |