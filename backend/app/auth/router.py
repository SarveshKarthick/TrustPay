from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth.schema import TokenResponse
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
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    try:
        return login_user(
            db,
            form_data
        )

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )