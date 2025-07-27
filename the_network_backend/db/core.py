# Author: Christopher Waschke
# Description: This file contains the database engine and session maker for SQLAlchemy.
# It uses asyncpg as the driver for PostgreSQL and is designed to be used with FastAPI.
# It also contains the configuration for the database connection, which is loaded from environment variables.

from sqlalchemy import create_engine, URL
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from the_network_backend.settings import config_dict



DB_URL = URL.create(
    drivername=config_dict["DB_DRIVER"],
    username=config_dict["DB_USER"],
    password=config_dict["DB_PASSWORD"],
    host=config_dict["DB_HOST"],
    port=config_dict["DB_PORT"],
    database=config_dict["DB_NAME"]
)

# Create our database engine. Using the the config_dict above to fill in the values
engine = create_async_engine(url=DB_URL)

# Create an async session maker
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

# Create our empty Declarative base class, as per SQLAlchemy documentation.
class Base(DeclarativeBase):
    pass