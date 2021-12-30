Feature: Assign Description

    Scenario: When I create a new ticket without description
        Given no description
        When call POST /tickets with specific description
        Then we will not create a ticket
    
    Scenario: When I create a new ticket with description
        Given a description
        When call POST /tickets with specific description
        Then we will create a ticket with description assigne