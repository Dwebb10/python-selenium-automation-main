
Feature: Cart functionality

    Scenario: user can search for a product on target
      Given open target homepage
      When search for a product
      Then verify search results are shown

  Scenario: Verify empty cart message is displayed
    Given open Target homepage
    When click on the Cart icon
    Then should see a message that my cart is empty
