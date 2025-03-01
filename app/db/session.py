from sqlmodel import create_engine, Session
from app.core.config import config

database_url  = ""

if config.db_type == "postgres":
    database_url="postgresql://characterapi:characterapi@db:5432/characterapi"
else:
    database_url="sqlite:///./database.db"

engine = create_engine(database_url, echo=config.debug)

def get_session():
    with Session(engine) as session:
        yield session