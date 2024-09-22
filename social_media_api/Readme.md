"""
Social Media API Project

Features:
- User registration and login.
- Token-based authentication using Django REST Framework.
- User profile management (bio, profile picture).
- Followers functionality (users can follow/unfollow each other).

Endpoints:
- POST /auth/register/ : Allows users to register.
- POST /auth/login/ : Handles user login and returns a token.
- GET /profile/ : Fetches the profile details of the authenticated user.
- PUT /profile/ : Updates the profile details of the authenticated user.

Tech Stack:
- Django: Web framework used for project structure.
- Django REST Framework: For creating APIs.
- DRF Authtoken: Token-based authentication.

How to Use:
- First, register a new user via the registration endpoint.
- Log in to retrieve a token.
- Use the token to make authenticated requests, such as viewing or updating your profile.
"""
