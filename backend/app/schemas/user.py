from pydantic import EmailStr, BaseModel, Field, ConfigDict

class UserCreate(BaseModel):
    username : str = Field(min_length=3, max_length=20)
    email : EmailStr 
    password : str = Field(min_length=8, max_length=128)

class LoginRequest(BaseModel):
    email : EmailStr 
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    email: EmailStr