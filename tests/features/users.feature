@initial
Feature: Generate users, groups and group permisions reading a permission file

  Background: 
    Given the User has a session open on Jazz

  @groups-permission @users @skip
  Scenario: Create Group
    When navigates to Groups
    Then clicks on New button
    Then enters the group name
    #Then selects a tenant
    #Then enters a set of group names
    #Then clicks on Save Changes button

  @groups-permission @admin @skip
  Scenario: Create Group from the django admin
    Then navigates to Django admin
    Then navigates to Admin-Groups
    Then clicks on Add button
    Then congifures the Group Permission
    #Then clicks on Save Group Permission button
