from app.core.config import settings
from app.core.exception import InvalidToken
import jwt

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.repositories.user_repository import UserRepo
from app.core.security import decode_access_token
from app.models.user import User
from app.core.exception import InvalidToken


oauth2_scheme = OAuth2PasswordBearer(tokenUrl= "/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    subject = decode_access_token(token)
    user_repo = UserRepo(db)
    try:
        user_id = int(subject)
    except ValueError:
        raise InvalidToken()
    user = user_repo.get_by_id(user_id)
    if user is None:
        raise InvalidToken()
    return user