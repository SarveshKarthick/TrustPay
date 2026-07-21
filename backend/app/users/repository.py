from sqlalchemy.orm import Session

from app.users.model import User


def get_user_by_email(
    db: Session,
    email: str
):
    return db.query(User).filter(
        User.email == email
    ).first()


def create_user(
    db: Session,
    user: User
):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_profile(
    db: Session,
    email: str
):
    return db.query(User).filter(
        User.email == email
    ).first()


def update_user_profile(
    db: Session,
    user: User,
    full_name: str,
    email: str
):
    user.full_name = full_name
    user.email = email

    db.commit()
    db.refresh(user)

    return user


def update_user_password(
    db: Session,
    user: User,
    password_hash: str
):
    user.password_hash = password_hash

    db.commit()
    db.refresh(user)

    return user