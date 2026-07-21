from pwdlib import PasswordHash
from datetime import datetime, timedelta, UTC
import jwt
from app.core.config import settings
from app.core.exception import InvalidToken

password_hasher = PasswordHash.recommended()

def hash_password (password: str) -> str:
    return password_hasher.hash(password)

def verify_password (password: str, hashed_password: str) -> bool:
    return password_hasher.verify(password, hashed_password)

def create_access_token(subject: str) -> str:
    expire = datetime.now(UTC) + timedelta(minutes=settings.access_token_expire_minutes)

    payload = {
        "sub" : str(subject),
        "exp" : expire
    }

    encoded_jwt = jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)

    return encoded_jwt

def decode_access_token(token: str) -> str:
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=settings.algorithm)
    
        subject = payload["sub"]
        if subject is None:
            raise InvalidToken()
        
        return subject
    
    except jwt.InvalidTokenError:
        raise InvalidToken()