from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate
from sqlalchemy.orm import Session
from app.database.session import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    pass