Feature: Edit Employee

    Scenario: When I edit a ticket without assignee
        Given no employee
        When call PUT /tickets with specific employee
        Then we will delete the employee assigned
    
    Scenario: When I edit a ticket with assignee
        Given a employee
        When call PUT /tickets with specific employee
        Then we update the employee assigned
