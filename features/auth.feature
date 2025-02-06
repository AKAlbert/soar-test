Feature: Authentication API Testing
    
    Scenario: Register new user
        Given I have valid user registration data
        When I send a POST request to "/client_registeration"
        Then the response status code should be 200
        And the response should contain "User Registered"

    Scenario: Login with registered user
        Given I have valid login credentials
        When I send a POST request to "/client_login"
        Then the response status code should be 200
        And the response should contain a JWT token

    Scenario: Register with existing email
        Given I have a registered user
        When I try to register with the same email
        Then the response should contain "Email already Exist" 

    Scenario: Login with invalid credentials
        Given I have invalid login credentials
        When I send a POST request to "/client_login"
        Then the response status code should be 401
        And the response should contain "Invalid credentials"

    Scenario: Login with valid credentials
        Given I have valid login credentials
        When I send a POST request to "/client_login"
        Then the response status code should be 200
        And the response should contain a JWT token

    Scenario: Logout
        Given I am logged in
        When I send a POST request to "/client_logout"
        Then the response status code should be 200
        And the response should contain "Logged out successfully"

