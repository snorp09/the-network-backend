from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..core import Base

if(TYPE_CHECKING):
    from .Post import Post

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()
    posts: Mapped[List["Post"]] = relationship("Post", back_populates="user")
    
    def __repr__(self):
        return f"Id: {self.id}, Username: {self.username}, Email: {self.email}"
