from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.schema import LoginRequest, TokenResponse
from app.auth.service import login_user
from app.dependencies.database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):
    try:
        return login_user(
            db,
            login_data
        )

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )