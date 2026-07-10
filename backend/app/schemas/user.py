from pydantic import EmailStr, BaseModel, Field

class UserCreate(BaseModel):
    username : str = Field(min_length=3, max_length=20)
    email : EmailStr 
    password : str = Field(min_length=8, max_length=128)
