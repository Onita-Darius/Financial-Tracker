from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User
from app.schemas.user import LoginRequest

class UserRepo:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id : int) -> User | None:
        query = select(User).where(User.id == user_id)
        result = self.db.execute(query)
        return result.scalar_one_or_none()

    def get_by_email(self, email : str) -> User | None:
        query = select(User).where(User.email == email)
        result = self.db.execute(query)
        return result.scalar_one_or_none()
    
    def create(self, user : User) -> User:
        self.db.add(user)
        self.db.flush()
        self.db.refresh(user)
        return user
