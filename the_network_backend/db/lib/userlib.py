# Author: Christopher Waschke
# Description: This file contains helper methods for user management in the database.

from ..core import SessionLocal
from ..models.User import User
from ..models import Post
from argon2 import PasswordHasher
from sqlalchemy import select

ph = PasswordHasher() # Password hashing object

class UserNotFoundException(Exception):
    """
    Thrown when a user is not found in the database.
    """
    pass

async def hash_password(passwd: str):
    """
    Hashes the password using the PasswordHasher object
    and returns the hashed password.

    Parameters:
        passwd (str): The password to hash.

    Returns:
        str: The hashed password.
    """
    passwd = ph.hash(passwd)
    return passwd

async def create_user(username: str, password: str, email: str) -> User:
    """
    Creates a new user in the database, and returns the user object.

    Parameters:
        username (str): The username of the user.
        password (str): The password of the user.
        email (str): The email of the user.

    Returns:
        User: The created user object.
    """
    new_user = User(
        username=username,
        password=await hash_password(password),
        email=email
    )
    
    async with SessionLocal() as sess:
        sess.add(new_user)
        await sess.commit()
        await sess.refresh(new_user)
    return new_user

async def get_user_by_email(email: str) -> User:
    """
    Gets a user from the database by their email.

    Parameters:
        email (str): The email of the user.

    Exceptions:
        UserNotFoundException: If the user is not found in the database.

    Returns:
        User: The user object.
    """
    async with SessionLocal() as sess:
        user = (await sess.execute(select(User).where(User.email == email))).one_or_none()
        if(user is None):
            raise UserNotFoundException()
        return user