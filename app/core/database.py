from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.core.config import settings

class Base(DeclarativeBase):
    pass

engine = create_engine(url=settings.DB_URL, connect_args={"check_same_thread" : False})

SessionLocal = sessionmaker(bind=engine, autoflush=False)

def create_tables():
    Base.metadata.create_all(bind=engine)