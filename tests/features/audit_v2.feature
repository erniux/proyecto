@audit
Feature: Work Audit Tasks for IA V2

  Background: 
    Given the User has a session open on Jazz

  @single_batch_all_locations
  Scenario: Create a Batch
    Then creates a Batch and assign it to a worker
    Then the worker works the Batch
    Then the worker post variances
    
  @batch_multiple_locations
  Scenario: Create a Batch that contains multiple active locations
    Then creates a Batch with multiple active locations and assign it to the worker
    Then the worker works the Batch
    Then the worker post variances

  @batch_reserve_locations
  Scenario: Create a Batch for reserve location with a parent container
    Then creates a Batch with one reserve location 

    