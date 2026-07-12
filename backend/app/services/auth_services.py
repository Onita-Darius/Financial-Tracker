from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.repositories.user_repository import UserRepo
from app.core.exception import EmailAlreadyExists
from app.core.security import hash_password

class AuthService:
    def __init__(self, db : Session):
        self.db = db
        self.user_repo = UserRepo(db)


    def register (self, user_data: UserCreate) -> User:
        
        try:
            existing_user = self.user_repo.get_by_email(user_data.email)

            if existing_user:
                raise EmailAlreadyExists()
            
            hashed_password = hash_password(user_data.password)

            user = User(
                username = user_data.username,
                email = user_data.email,
                password_hash = hashed_password,
            )

            self.user_repo.create(user)

            self.db.commit()

            return user
        except Exception:
            self.db.rollback()
            raise
        