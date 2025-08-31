@inventory
Feature: Inventory 

  Background: 
    Given the User has a session open on Jazz

  @adjustment
  Scenario: Create an Adjustment for Invata Tenants
    Then navigates to create an adjustment
    Then selects a facility
    Then create an adjustment


  Scenario: Create an ASN
    Then creates an ASN
    Then navigates to the ASN
    Then validates the data

     
     