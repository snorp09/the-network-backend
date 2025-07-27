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
        user = (await sess.execute(select(User).where(User.email == email))).scalar_one_or_none()
        if(user is None):
            raise UserNotFoundException()
        return user

async def login_user(email: str, password: str) -> User:
    """
    Logs in a user by verifying their email and password.

    Parameters:
        email (str): The email of the user.
        password (str): The password of the user.

    Returns:
        User: The user object if login is successful.

    Raises:
        UserNotFoundException: If the user is not found or the password is incorrect.
    """
    user = await get_user_by_email(email)
    
    if not ph.verify(user.password, password):
        raise UserNotFoundException("Invalid credentials")
    
    return user

async def update_user_password(user: User, new_password: str) -> User:
    """
    Updates the password of a user in the database.

    Parameters:
        user (User): The user object to update.
        new_password (str): The new password to set.

    Returns:
        User: The updated user object.
    """
    user.password = await hash_password(new_password)
    
    async with SessionLocal() as sess:
        sess.add(user)
        await sess.commit()
        await sess.refresh(user)
    
    return user