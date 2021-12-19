Feature: Select Ticket

    Scenario: When I select a ticket it return the selected one
        Given an id
        When call get /tickets/id
        Then we will get the selected ticket