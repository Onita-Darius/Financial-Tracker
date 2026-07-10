from app.core.config import settings
from sqlalchemy import create_engine

engine = create_engine(
    settings.database_url,
    echo=True
)
print("Testing: " + settings.database_url)