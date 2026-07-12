from fastapi import FastAPI
from sqlalchemy import text
from app.database.session import engine

from app.api.auth import router as auth_router

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "test"}

app.include_router(auth_router)