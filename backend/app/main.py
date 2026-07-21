from fastapi import FastAPI
from sqlalchemy import text
from app.database.session import engine

from app.api.auth import router as auth_router
from app.api.users import router as user_router

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "test"}

app.include_router(auth_router)
app.include_router(user_router)