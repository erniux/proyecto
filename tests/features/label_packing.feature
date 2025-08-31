@labelpacking
Feature: Label Packing

    Create a label packing for a single order
    


    Background:
        Given the User has a session open on Jazz

    @skip
    Scenario: Label Packing
        When the user selects 8 order for label packing wave
        #Then the user work the label pull task
        #Then the user does the packing label task