@orders
Feature: Create Orders
  Select diferent paths to create orders on Jazz
  UI
  API
  menu
  URL

  Background:
    Given the User has a session open on Jazz


  @api 
  Scenario Outline: API Import an order
    Given the order is created with a payload
    When validates the order status
    Then if the order status is "New", the user triggers the celey task
    Then if the order status is "Allocated", the user triggers the celey task
    Then validates the order status
    Examples:
        | execution |
        | 1         |
        | 2         |
        | 3         |
        | 4         | 


  @ui 
  Scenario: Create an order
    When navigates to create an order
    Then selects a Source Code
    Then searches for the item
    Then searches for the sku
    Then selects the quantity of the item
    Then adds the items to the order
    Then selects a shipping method
    Then selects a customer
    Then selects a ship to address same as customer
    Then adds the payment details same as customer
    Then clicks on Create Order button
    When validates the order status
    Then if the order status is "New", the user triggers the celey task
    Then if the order status is "Allocated", the user triggers the celey task
    Then validates the order status

  @ui-multiple-items
  Scenario: Create an order with multiple items
    When navigates to create an order
    Then selects a Source Code
    Then adds "10" items
    Then selects a shipping method
    Then selects a customer
    Then selects a ship to address same as customer
    Then adds the payment details same as customer
    Then clicks on Create Order button
    When validates the order status
    Then if the order status is "New", the user triggers the celey task
    Then if the order status is "Allocated", the user triggers the celey task
    Then validates the order status






