from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = URL.create(
    "mysql+pymysql",
    username="root",
    password="Aditya@123",
    host="localhost",
    database="student",
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base.metadata.create_all(bind=engine)