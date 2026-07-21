from fastapi import APIRouter, Depends, HTTPException, status
from app.models.user import User
from app.schemas.user import UserResponse
from app.auth.dependencies import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@router.get(
        "/me",
        response_model=UserResponse)
def get_me(curenet_user:User = Depends(get_current_user)):
    return curenet_user