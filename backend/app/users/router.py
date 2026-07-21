from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.dependencies.database import get_db
from app.users.schema import (
    ChangePasswordRequest,
    UserCreate,
    UserProfileResponse,
    UserResponse,
    UserUpdateRequest,
)
from app.users.service import (
    change_current_user_password,
    get_current_user_profile,
    register_user,
    update_current_user_profile,
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    try:
        return register_user(db, user)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/me",
    response_model=UserProfileResponse
)
def get_me(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        return get_current_user_profile(
            db,
            current_user
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.put(
    "/me",
    response_model=UserProfileResponse
)
def update_me(
    user: UserUpdateRequest,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        return update_current_user_profile(
            db,
            current_user,
            user
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.put("/change-password")
def change_password(
    password_data: ChangePasswordRequest,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        change_current_user_password(
            db,
            current_user,
            password_data
        )

        return {
            "message": "Password changed successfully"
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )