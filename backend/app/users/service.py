from app.auth.security import hash_password
from sqlalchemy.orm import Session

from app.users.model import User
from app.users.schema import UserCreate
from app.users.repository import get_user_by_email, create_user


def register_user(db: Session, user_data: UserCreate):

    # Check if email already exists
    existing_user = get_user_by_email(db, user_data.email)

    if existing_user:
        raise ValueError("Email already registered")

    # Hash password
    hashed_password = hash_password(user_data.password)

    # Create user object
    user = User(
        full_name=user_data.full_name,
        email=user_data.email,
        password_hash=hashed_password
    )

    # Save user
    return create_user(db, user)