from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from collections.abc import Generator

engine = create_engine(
    settings.database_url,
    echo=True
)

def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

#* This is the old way, no longer recomanded in SQLAlchemy doc

# SessionLocal = sessionmaker(
#     bind = engine,
#     autoflush = False,
#     autocommit = False,
# )

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close