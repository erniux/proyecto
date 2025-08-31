@initial
Feature: Generate initial data to work on local environment

  Background: 
    Given the User has a session open on Jazz

  @system-tenant-facility  
  Scenario: Generates System data
    #Then creates a Tenant
    #Then creates a facility
    #Then adds facility to user profile
    #Then adds facility to Tenant
    #Then setups control settings

  @system @config
  Scenario: Generates System Client Setup data
    #Then adds default allocation rules
    #Then creates workstations
    #Then creates Appeasement types
    #Then creates business types
    #Then creates offers
    #Then creates sources
    #Then creates cancelation reasons
    #Then creates exception reasons
    #Then creates exception resolution reasons
    #Then creates hold reasons
    #Then adds inventory transaction reasons
    #Then creates override reasons
    #Then adds card payments
    

  @shipping  @config
  Scenario: Generates System Shipping data
    #Then creates carriers
    #Then creates ship codes
    #Then adds flat rates
    #Then adds shipping method and cartons to facility
    #Then creates disposition codes

  @wms @config
  Scenario: Generates wms data for locations and carts
    #Then creates locations
    #Then creates shipping carts   

  @items  
  Scenario: Generates items for existing Tenant
    Then creates items and skus
    #Then creates items with lots
    #Then creates items with kits
    #Then creates virtual items
    #Then create Price Groups to items

  @validates-inventory 
  Scenario: Validates all data can be used
    Then receive inventory
    Then putaway inventory



  

  

