from fastapi import FastAPI
from app.core.config import settings
from sqlalchemy import text
from app.database.session import engine


app = FastAPI()

@app.get("/")
def root():
    return {"message" : settings.database_url}