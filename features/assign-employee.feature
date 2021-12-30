Feature: Assign Employee

    Scenario: When I create a new ticket without assignee
        Given no employee
        When call POST /tickets with specific employee
        Then we will create a ticket with no employee assigned
    
    Scenario: When I create a new ticket with assignee
        Given a employee
        When call POST /tickets with specific employee
        Then we will create a ticket with employee assigne
