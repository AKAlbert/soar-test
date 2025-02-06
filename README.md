# Flask Authentication API

A simple Flask-based authentication API that provides user registration, login, and logout functionality with JWT token-based authentication.

## Features

- User Registration
- User Login with JWT token
- User Logout
- BDD Testing with Behave

## Prerequisites

- Python 3.x
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone </Software-Engineering-Test/Flask-Authentication-API>
cd <project-directory>

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- On Windows:
```bash
venv\Scripts\activate
```
- On macOS/Linux:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Dependencies

- Flask: Web framework
- PyJWT: JWT token handling
- Behave: BDD testing framework

## Development

To add new features:
1. Write feature files in the `features` directory
2. Implement step definitions in `features/steps`
3. Add new routes in `app.py`

## Security Notes

This is a basic implementation. For production use, consider adding:
- Password hashing
- Token blacklisting
- Input validation
- Database persistence
- Rate limiting
- CORS configuration
- Environment variables for secrets

## Running the tests

To run the tests, use the following command:
```bash
behave /features/feature_name.feature
```
