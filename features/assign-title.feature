Feature: Assign Title

    Scenario: When I create a new ticket without title
        Given no title
        When call POST /tickets with specific title
        Then we will not create a ticket
    
    Scenario: When I create a new ticket with title
        Given a title
        When call POST /tickets with specific title
        Then we will create a ticket with title assigne