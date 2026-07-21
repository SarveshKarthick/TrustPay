from sqlalchemy.orm import Session

from app.auth.security import (
    hash_password,
    verify_password
)
from app.users.model import User
from app.users.repository import (
    create_user,
    get_user_by_email,
    get_user_profile,
    update_user_password,
    update_user_profile
)
from app.users.schema import (
    ChangePasswordRequest,
    UserCreate,
    UserUpdateRequest
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


def change_current_user_password(
    db: Session,
    current_email: str,
    password_data: ChangePasswordRequest
):
    current_user = get_user_profile(
        db,
        current_email
    )

    if not current_user:
        raise ValueError("User not found")

    if not verify_password(
        password_data.current_password,
        current_user.password_hash
    ):
        raise ValueError("Current password is incorrect")

    new_password_hash = hash_password(
        password_data.new_password
    )

    return update_user_password(
        db,
        current_user,
        new_password_hash
    )