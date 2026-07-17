from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth.security import (
    verify_password,
    create_access_token
)
from app.users.repository import get_user_by_email


def login_user(
    db: Session,
    form_data: OAuth2PasswordRequestForm
):
    # Find user by email
    user = get_user_by_email(
        db,
        form_data.username
    )

    if not user:
        raise ValueError("Invalid email or password")

    # Verify password
    if not verify_password(
        form_data.password,
        user.password_hash
    ):
        raise ValueError("Invalid email or password")

    # Generate JWT
    access_token = create_access_token(
        data={
            "sub": user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }