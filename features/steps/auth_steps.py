from behave import given, when, then
import json
from app import app

# Test data
TEST_USER = {
    "email": "test@example.com",
    "password": "test123",
    "name": "Test User"
}

@given('I have valid user registration data')
def step_impl(context):
    context.client = app.test_client()
    context.data = TEST_USER

@given('I have valid login credentials')
def step_impl(context):
    context.client = app.test_client()
    context.data = {
        "email": TEST_USER["email"],
        "password": TEST_USER["password"]
    }

@given('I have invalid login credentials')
def step_impl(context):
    context.client = app.test_client()
    context.data = {
        "email": "wrong@example.com",
        "password": "wrongpass"
    }

@given('I have a registered user')
def step_impl(context):
    context.client = app.test_client()
    # First register a user
    response = context.client.post(
        '/client_registeration',
        json=TEST_USER,
        content_type='application/json'
    )
    # Don't assert status code here since we want to test duplicate registration
    context.data = TEST_USER

@given('I am logged in')
def step_impl(context):
    context.client = app.test_client()
    # Login and store the token
    login_data = {
        "email": TEST_USER["email"],
        "password": TEST_USER["password"]
    }
    # First register the user
    context.client.post(
        '/client_registeration',
        json=TEST_USER,
        content_type='application/json'
    )
    # Then login
    response = context.client.post(
        '/client_login',
        json=login_data,
        content_type='application/json'
    )
    assert response.status_code == 200
    context.token = json.loads(response.data)['token']
    # Set empty data for logout request
    context.data = {}

@when('I send a POST request to "{endpoint}"')
def step_impl(context, endpoint):
    headers = {}
    if hasattr(context, 'token'):
        headers['Authorization'] = f'Bearer {context.token}'
    
    context.response = context.client.post(
        endpoint,
        json=context.data,
        headers=headers,
        content_type='application/json'
    )

@when('I try to register with the same email')
def step_impl(context):
    # Ensure we're using the same TEST_USER data
    context.response = context.client.post(
        '/client_registeration',
        json=TEST_USER,
        content_type='application/json'
    )

@then('the response status code should be {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code, \
        f"Expected status code {status_code} but got {context.response.status_code}. Response: {context.response.data}"

@then('the response should contain "{text}"')
def step_impl(context, text):
    response_data = context.response.data.decode('utf-8')
    assert text in response_data, f"Expected '{text}' in response but got: {response_data}"

@then('the response should contain a JWT token')
def step_impl(context):
    response_data = json.loads(context.response.data)
    assert 'token' in response_data
    assert response_data['token'] is not None 