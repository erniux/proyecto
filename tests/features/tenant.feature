@tenants
Feature: Create and Edit Tenant

Background: 
    Given the User has a session open on Jazz

  @skip
  Scenario: Create a tenant
    When navigates to the menu "System"
    When navigates to the menu "Tenants"
    Then clicks on New Button
    Then enters the tenant details
    Then enters the time zone
    Then enters the contact details
    Then enters the messaging details
    Then enters the emails domains
    Then enters the general settings
    Then enters the carrier notifications
    Then enters the integration settings
    Then enters the payment settings
    Then enters the warehouse settings
    Then enterrs the virtual shipment settings
    Then enters the sftp settings
    Then selects the facilities
    Then selects Facility for returns
    Then clicks on Save Changes button