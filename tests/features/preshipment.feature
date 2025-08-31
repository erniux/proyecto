Feature: Preshipment Label and Carton Handling

  Background:
    Given a pick/tote is loaded

  Scenario: Preshipment exists with valid label and carton, all units packed
    Given a preshipment exists for the pick
    And the label is valid
    And the carton used matches the preshipment carton
    And all units are packed
    When the packer proceeds with packing
    Then the label is sent to the printer
    And the preshipment is converted to a shipment

  Scenario: Preshipment exists but packer changes carton
    Given a preshipment exists for the pick
    And the label is valid
    And the carton used does not match the preshipment carton
    When the packer proceeds with packing
    Then the proposed preshipment flow is cancelled
    And the system proceeds with the default packing flow

  Scenario: Preshipment exists but not all units are packed
    Given a preshipment exists for the pick
    And the label is valid
    And the carton used matches the preshipment carton
    But not all units are packed
    When the packer proceeds with packing
    Then the proposed preshipment flow is cancelled
    And the system proceeds with the default packing flow

  Scenario: No preshipment exists
    Given no preshipment exists for the pick
    When the packer proceeds with packing
    Then the system proceeds with the default packing flow

  Scenario: Preshipment exists but label is invalid
    Given a preshipment exists for the pick
    But the label is invalid
    When the packer proceeds with packing
    Then the system proceeds with the default packing flow

  Scenario: Preshipment exists, label valid, carton missing
    Given a preshipment exists for the pick
    And the label is valid
    But the carton data is missing
    When the packer proceeds with packing
    Then the system proceeds with the default packing flow
