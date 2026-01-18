# backend/routes/auth.py

from fastapi import APIRouter, HTTPException, status
from models.user import User
from services.auth_service import register_user, get_user

router = APIRouter()

# -----------------------------
# Register User
# -----------------------------
@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: User):
    try:
        new_user = register_user(user)
        return {
            "message": "User registered successfully",
            "user": new_user
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# -----------------------------
# Get User by Username
# -----------------------------
@router.get("/user/{username}")
def fetch_user(username: str):
    try:
        user = get_user(username)
        return user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
