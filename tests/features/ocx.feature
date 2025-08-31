Feature: CASI Automated Packing Workflow
  Description: Test cases for the conveyor-belt picking workflow, 
  including LPN assignment, picking, auditing, label generation, 
  conveyor processing, wave creation, and packout.


  # LPN Assignment to Orders
  Scenario: Assign LPN to Next Available Order (Workflow A)
    Given a wave has been created with multiple unassigned orders
    And the user is on the "Assign LPN to Order" screen in CASI
    When the user scans an LPN barcode "LPN123"
    Then the system assigns "LPN123" to the next available order
    And a new batch is created with "LPN123" as the tote barcode
    And the batch status is updated to "Assigned"
    And the pick is created on the order, determining the shipping carton based on SKU, dims, and dimming algorithm

  Scenario: Assign LPN to Specific Order via Packing Slip (Workflow B)
    Given a wave has been created with an order "ORD456"
    And the user is on the "Assign LPN to Order" screen in CASI
    When the user scans a packing slip barcode linked to "ORD456"
    Then the system assigns a new LPN (e.g., "LPN789") to "ORD456"
    And a new batch is created with "LPN789" as the tote barcode
    And the batch status is updated to "Assigned"
    And the pick is associated with the shipping carton determined by SKU, dims, and dimming algorithm

  Scenario: LPN Already Assigned to Another Order
    Given LPN "LPN123" is already assigned to order "ORD111"
    And the user is on the "Assign LPN to Order" screen in CASI
    When the user scans LPN "LPN123"
    Then the system displays an error message "LPN already assigned to another order"
    And no new batch is created
    And the system logs the error for audit


  # Picker Dashboard and Picking Process
  Scenario: Successful Pick with LPN and Location Scan
    Given a batch with LPN "LPN123" is assigned to a wave
    And the wave includes items: SKU "ABC123", qty 2, location "Bay1-A1"
    And the picker is on the "Picker Dashboard" screen in CASI
    When the picker selects "Bay1" as their station
    And the picker scans LPN "LPN123" using a tablet
    And the system displays the pick list: SKU "ABC123", qty 2, location "Bay1-A1"
    And the picker scans location barcode "Bay1-A1"
    Then the system confirms the pick
    And the pick status is updated to "Picked" for 2 units of "ABC123"
    And a save_progress call records the update in Jazz
    And the picked units are recorded in the audit table

  Scenario: Incorrect Location Barcode Scanned
    Given a batch with LPN "LPN123" is assigned to a wave
    And the wave includes items: SKU "ABC123", qty 2, location "Bay1-A1"
    And the picker is on the "Picker Dashboard" screen in CASI
    When the picker selects "Bay1" as their station
    And the picker scans LPN "LPN123"
    And the picker scans location barcode "Bay2-B2" (incorrect)
    Then the system displays an error "Incorrect location scanned"
    And the pick status remains "Not Picked"
    And the error is logged in the audit table for review

  Scenario: Exception Flagged for Missing Item
    Given a batch with LPN "LPN123" is assigned to a wave
    And the wave includes items: SKU "ABC123", qty 2, location "Bay1-A1"
    And the picker is on the "Picker Dashboard" screen in CASI
    When the picker selects "Bay1" as their station
    And the picker scans LPN "LPN123"
    And the picker does not scan the location barcode for "Bay1-A1"
    And the picker completes the bay
    Then the system marks SKU "ABC123" as an exception in the save_progress call
    And the pick status remains "Not Picked"
    And the exception is recorded in the audit table for triage workflow


  # Auditor Scans LPN on Conveyor
  Scenario: Successful Auditor Verification
    Given a batch with LPN "LPN123" is on the conveyor after picking
    And the wave includes items: SKU "ABC123", qty 2, location "Bay1-A1"
    And the picker has completed the pick and marked units as picked
    When the auditor scans LPN "LPN123" using a tablet at the conveyor
    Then the system displays picked units to audit
    And the auditor confirms the units as audited
    And the audit status is updated in the audit table

  Scenario: Auditor Identifies Discrepancy
    Given a batch with LPN "LPN123" is on the conveyor after picking
    And the wave includes items: SKU "ABC123", qty 2, location "Bay1-A1"
    And the picker marked 2 units as picked, but only 1 unit was actually picked
    When the auditor scans LPN "LPN123" using a tablet at the conveyor
    Then the system displays picked units to audit
    And the auditor identifies a discrepancy (1 unit missing)
    And the system logs the discrepancy in the audit table
    And triggers a triage workflow for exceptions


  # Asynchronous Label Generation
  @async-label-generation @skip
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


  @async-label-generation  
  Scenario: Successful Label Generation
    Given a wave is created with orders and conveyor cart
    When the system triggers the TMS API with order details 
    Then the TMS returns labels "LBL001" and "LBL002" with tracking numbers
    And the labels are stored in the shipping pre-shipment model with pick_ids
    And the labels are associated with the shipping carton determined by SKU, dims, and dimming algorithm

  Scenario: TMS Failure with Fallback
    Given a wave is created with order "ORD001"
    And the cart type is set to "Conveyor Workflow"
    When the system triggers the TMS API with order details
    And the TMS API fails to respond
    Then the system generates a fallback shipping label "FBL001"
    And the label is stored in the shipping.pre_shipment model with pick_id
    And the system logs the failure in the audit table
    And a task is created in Celery to catch the failed shipment call


  # Conveyor and Label Application
  Scenario: Successful Label Application
    Given a batch with LPN "LPN123" is on the conveyor
    And a pre-generated label "LBL001" with tracking "TRK123" is stored for "LPN123"
    When the box reaches the label station
    Then CASI retrieves and prints label "LBL001"
    And CASI applies the label to the box
    And a shipment record is created in Jazz with status "Shipped"
    And the shipment is recorded in the audit table

  Scenario: Missing Label at Conveyor End
    Given a batch with LPN "LPN123" is on the conveyor
    And no pre-generated label exists for "LPN123"
    When the box reaches the label station
    Then CASI flags an error "No label available for LPN123"
    And the system logs the error in the audit table
    And the shipment record is not created
    And a task is triggered in Celery to handle the failed shipment call

  # Wave Creation and Integration
  Scenario: Wave Creation Triggers TMS and Carton Assignment
    Given orders "ORD001" and "ORD002" are grouped into a wave
    And the user selects a shipping carton as a filter in CASI
    And the cart type is set to "Conveyor Workflow"
    When the user creates the wave
    Then the system triggers TMS label generation asynchronously
    And the batch status for each order is set to "Pending"
    And the system assigns picks to the shipping carton based on SKU, dims, and dimming algorithm
    And the picks are recorded in Jazz

  Scenario: Wave Creation Fails Due to Invalid Carton Selection
    Given orders "ORD001" and "ORD002" are grouped into a wave
    And the user selects an invalid shipping carton (e.g., incompatible dims)
    And the cart type is set to "Conveyor Workflow"
    When the user attempts to create the wave
    Then the system displays an error "Invalid shipping carton selected"
    And no wave is created
    And the error is logged in the audit table

  # Automatic Packout
  Scenario: Successful Automatic Packout
    Given a batch with LPN "LPN123" is completed on the conveyor
    And the auditor has audited and confirmed all picked units
    When the system processes the batch for automatic packout
    Then CASI finalizes the packout
    And the shipment record is updated in Jazz with status "Shipped"
    And the packout is recorded in the audit table

  Scenario: Fallback to Standard Jazz Packing
    Given a batch with LPN "LPN123" is completed on the conveyor
    And the automatic packout process fails due to a system error
    When the system detects the failure
    Then the system routes the batch to standard Jazz packing
    And the user scans the LPN on the Jazz Packing Screen
    And a shipping carton is pre-selected and a shipment record is created in Jazz
    And the error is logged in the audit table