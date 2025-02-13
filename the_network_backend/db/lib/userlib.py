from ..core import SessionLocal
from ..models.User import User
from ..models import Post

async def hash_password(passwd: str):
    # TODO Hash passwords.
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
