from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, mapped_column
from ..core import Base

if(TYPE_CHECKING):
    from .Post import Post

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()
    posts: Mapped[List["Post"]] = mapped_column(back_populates="user")
