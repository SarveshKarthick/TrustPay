from sqlalchemy.orm import Session

from app.auth.security import (
    verify_password,
    create_access_token
)
from app.auth.schema import LoginRequest
from app.users.repository import get_user_by_email


def login_user(db: Session, login_data: LoginRequest):

    # Find user by email
    user = get_user_by_email(
        db,
        login_data.email
    )

    # Email not found
    if not user:
        raise ValueError("Invalid email or password")

    # Wrong password
    if not verify_password(
        login_data.password,
        user.password_hash
    ):
        raise ValueError("Invalid email or password")

    # Generate JWT Token
    access_token = create_access_token(
        data={
            "sub": user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }