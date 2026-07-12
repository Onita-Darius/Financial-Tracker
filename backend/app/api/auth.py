from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate
from app.database.session import get_db
from app.services.auth_services import AuthService
from app.core.exception import EmailAlreadyExists

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.post(
        "/register",
        status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    auth_services = AuthService(db)
    try:
        return auth_services.register(user)
    except EmailAlreadyExists as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e),
        )