Feature: Edit State

    Scenario: When create a ticket is set as OPEN
        Given no state
        When call POST /tickets with specific state
        Then ticket created with correct state
    
    Scenario: When set a ticket as IN_PROGRESS
        Given IN_PROGRESS state
        When call PUT /tickets with specific state
        Then set correct state

    Scenario: When set a ticket as WAITING_DEVELOP
        Given WAITING_DEVELOP state
        When call PUT /tickets with specific state
        Then set correct state

    Scenario: When set a ticket as WAITING_CLIENT
        Given WAITING_CLIENT state
        When call PUT /tickets with specific state
        Then set correct state
    
    Scenario: When set a ticket as CLOSE
        Given CLOSE state
        When call PUT /tickets with specific state
        Then set correct state
