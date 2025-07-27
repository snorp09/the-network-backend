from dotenv import load_dotenv
from os import environ

# Load environment variables from .env file
load_dotenv()

# Dictionary to hold database configuration
config_dict = {
    "DB_DRIVER": "postgresql+asyncpg",
    "DB_USER": environ.get("DB_USER"),
    "DB_PASSWORD": environ.get("DB_PASSWORD"),
    "DB_HOST": environ.get("DB_HOST"),
    "DB_PORT": environ.get("DB_PORT"),
    "DB_NAME": environ.get("DB_NAME"),
    "JWT_SECRET": environ.get("JWT_SECRET"),
}