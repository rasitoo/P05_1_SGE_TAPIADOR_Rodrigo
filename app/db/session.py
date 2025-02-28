from sqlmodel import create_engine, Session
from app.core.config import config

database_url  = ""

if config.db_type == "postgres":
    database_url="postgresql://postgres:123456@127.0.0.1:5432/dummy"
else:
    database_url="sqlite:///./database.db"

engine = create_engine(config.database_url, echo=config.debug)

def get_session():
    with Session(engine) as session:
        yield session