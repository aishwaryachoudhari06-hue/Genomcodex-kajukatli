# backend/services/auth_service.py

"""
Authentication and user-related business logic.
Uses fake_db for now.
Later, this will connect to MongoDB.
"""

from models.user import User
from services.fake_db import add_user, get_user_by_username


# -----------------------------
# Register a new user
# -----------------------------
def register_user(user: User):
    """
    Registers a new user if username does not already exist.
    """

    existing_user = get_user_by_username(user.username)

    if existing_user:
        raise ValueError("User already exists")

    # Convert Pydantic model to dictionary
    user_data = user.dict()

    add_user(user_data)

    return user_data


# -----------------------------
# Simple user lookup
# -----------------------------
def get_user(username: str):
    """
    Returns user data if user exists.
    """

    user = get_user_by_username(username)

    if not user:
        raise ValueError("User not found")

    return user
