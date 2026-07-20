from app.auth.security import hash_password
from sqlalchemy.orm import Session

from app.users.model import User
from app.users.schema import (
    UserCreate,
    UserUpdateRequest
)
from app.users.repository import (
    get_user_by_email,
    create_user,
    get_user_profile,
    update_user_profile
)


def register_user(
    db: Session,
    user_data: UserCreate
):
    existing_user = get_user_by_email(
        db,
        user_data.email
    )

    if existing_user:
        raise ValueError("Email already registered")

    hashed_password = hash_password(
        user_data.password
    )

    user = User(
        full_name=user_data.full_name,
        email=user_data.email,
        password_hash=hashed_password
    )

    return create_user(
        db,
        user
    )


def get_current_user_profile(
    db: Session,
    email: str
):
    user = get_user_profile(
        db,
        email
    )

    if not user:
        raise ValueError("User not found")

    return user


def update_current_user_profile(
    db: Session,
    current_email: str,
    user_data: UserUpdateRequest
):
    current_user = get_user_profile(
        db,
        current_email
    )

    if not current_user:
        raise ValueError("User not found")

    existing_user = get_user_by_email(
        db,
        user_data.email
    )

    if (
        existing_user
        and existing_user.id != current_user.id
    ):
        raise ValueError("Email already registered")

    return update_user_profile(
        db,
        current_user,
        user_data.full_name,
        user_data.email
    )