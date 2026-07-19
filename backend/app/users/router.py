from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.dependencies.database import get_db
from app.users.schema import (
    UserCreate,
    UserResponse,
    UserProfileResponse
)
from app.users.service import (
    register_user,
    get_current_user_profile
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