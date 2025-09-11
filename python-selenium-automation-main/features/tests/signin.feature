Feature: Sign In functionality

  Scenario: Verify logged out user can navigate to Sign In
    Given open Target homepage
    When user clicks on the Sign In link
    Then verify sign in page shows

