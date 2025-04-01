from ..core import SessionLocal
from ..models.User import User
from ..models import Post
from argon2 import PasswordHasher
from sqlalchemy import select

ph = PasswordHasher()

class UserNotFoundException(Exception):
    pass

async def hash_password(passwd: str):
    passwd = ph.hash(passwd)
    return passwd

async def create_user(username: str, password: str, email: str) -> User:

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
    async with SessionLocal() as sess:
        user = (await sess.execute(select(User).where(User.email == email))).one_or_none()
        if(user is None):
            raise UserNotFoundException()
        return user