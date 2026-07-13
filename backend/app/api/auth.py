from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, Token, LoginRequest
from app.database.session import get_db
from app.services.auth_services import AuthService
from app.core.exception import EmailAlreadyExists, InvalidUser

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
    
@router.post(
    "/login",
    response_model=Token)
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    auth_services = AuthService(db)
    try:
        return auth_services.login(login_data)
    except InvalidUser as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
        )