from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, LoginRequest, Token
from app.repositories.user_repository import UserRepo
from app.core.exception import EmailAlreadyExists, InvalidUser
from app.core.security import hash_password, verify_password, create_access_token

class AuthService:
    def __init__(self, db : Session):
        self.db = db
        self.user_repo = UserRepo(db)


    def register (self, user_data: UserCreate) -> User:
        
        try:
            existing_user = self.user_repo.get_by_email(user_data.email)
            print(existing_user)

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
        
    def login(self, login_data: LoginRequest) ->  Token:
        
        user = self.user_repo.get_by_email(login_data.email)
        
        print(f"USER RESULT: {user}, {user.email}, {user.password_hash}")
        if user is None:
            raise InvalidUser()
        
        if not verify_password(login_data.password, user.password_hash):
            raise InvalidUser()
        
        token = create_access_token(user.id)
        
        return Token(
                    access_token=token,
                    token_type="bearer"
                )    
        
