from sqlalchemy import create_engine, URL
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from os import environ

config_dict = {
    "DB_DRIVER": "postgresql+asyncpg",
    "DB_USER": environ.get("DB_USER"),
    "DB_PASSWORD": environ.get("DB_PASSWORD"),
    "DB_HOST": environ.get("DB_HOST"),
    "DB_PORT": environ.get("DB_PORT")
}

engine = create_async_engine(
    URL.create(
        drivername=config_dict["DB_DRIVER"],
        username=config_dict["DB_USER"],
        password=config_dict["DB_PASSWORD"],
        host=config_dict["DB_HOST"],
        port=config_dict["DB_PORT"],
    )
)

SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass