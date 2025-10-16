Feature: Target cart functionality

  Scenario: Cart shows "Your cart is empty" when there are no items
    Given Open Target homepage
    When I click the cart icon
    Then Verify that "Your cart is empty" message is shown

  Scenario: Add a product to the cart and verify it appears
    Given Open Target homepage
    When I search for "knife"
    And I select the first product from results
    And I add the product to the cart
    And I go to the cart page
    Then Verify that the cart has items



