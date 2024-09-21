# cg4

# Social Media API

## Project Setup

1. Clone the repository (Alx_DjangoLearnLab).
2. Create a virtual environment and activate it.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Set up the database using `python manage.py migrate`.
5. Create a superuser using `python manage.py createsuperuser`.
6. Run the development server using `python manage.py runserver`.

## API Endpoints

- `/api/accounts/register/` - Register a new user.
- `/api/accounts/login/` - Log in and retrieve an authentication token.
- `/api/accounts/profile/` - View and update user profile (authenticated).

## Authentication
- Token-based authentication is used. After login, include the token in the header as `Authorization: Token <token>`.


# OR_ppty

# Social Media API

## Overview

This is a simple Social Media API built using Django and Django REST Framework.

## Setup Instructions

1. Install dependencies:
   
   ```bash
   pip install django djangorestframework djangorestframework-authtoken

2. Create migrations and migrate the database:

python manage.py makemigrations accounts
python manage.py migrate

3. Start the server:

python manage.py runserver

User Authentication Endpoints

Register User

- Endpoint: /api/accounts/register/
- Method: POST
- Request Body:
json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "password123"
}

Login User
- Endpoint: /api/accounts/login/
- Method: POST
- Request Body:
json
{
  "username": "testuser",
  "password": "password123"
}
- Response on Success:
json
{
  "token": "<your_token_here>"
}

### Conclusion

You have successfully set up a foundational Social Media API with user authentication using Django and Django REST Framework. This includes creating custom user models, implementing registration and login functionality, and preparing your project for further development of social media features! You can now expand this API with additional functionalities like posting content, following users, or commenting on posts as needed.