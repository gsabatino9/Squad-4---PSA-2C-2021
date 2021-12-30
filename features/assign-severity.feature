Feature: Assign Severity

    Scenario: When I create a new ticket without severity
        Given no severity
        When call POST /tickets with specific severity
        Then we will not create a ticket
    
    Scenario: When I create a new ticket with severity
        Given a severity
        When call POST /tickets with specific severity
        Then we will create a ticket with severity assigne