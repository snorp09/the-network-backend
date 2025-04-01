# Author: Christopher Waschke
# Description: This file contains the database engine and session maker for SQLAlchemy.
# It uses asyncpg as the driver for PostgreSQL and is designed to be used with FastAPI.
# It also contains the configuration for the database connection, which is loaded from environment variables.

from sqlalchemy import create_engine, URL
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from os import environ
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Dictionary to hold database configuration
config_dict = {
    "DB_DRIVER": "postgresql+asyncpg",
    "DB_USER": environ.get("DB_USER"),
    "DB_PASSWORD": environ.get("DB_PASSWORD"),
    "DB_HOST": environ.get("DB_HOST"),
    "DB_PORT": environ.get("DB_PORT"),
    "DB_NAME": environ.get("DB_NAME")
}

DB_URL = URL.create(
    drivername=config_dict["DB_DRIVER"],
    username=config_dict["DB_USER"],
    password=config_dict["DB_PASSWORD"],
    host=config_dict["DB_HOST"],
    port=config_dict["DB_PORT"],
    database=environ.get("DB_NAME")
)

# Create our database engine. Using the the config_dict above to fill in the values
engine = create_async_engine(url=DB_URL)

# Create an async session maker
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

# Create our empty Declarative base class, as per SQLAlchemy documentation.
class Base(DeclarativeBase):
    pass