from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..core import Base

if(TYPE_CHECKING):
    from .Post import Post

# Our User model, which is used to represent a user in the database.
# It contains the following fields:
# - id: The primary key for the user. This is an auto-incrementing integer.
# - username: The username of the user. This is a string.
# - email: The email of the user. This is a string.
# - password: The password of the user. This is a string.
# - posts: A list of posts made by the user. This is a one-to-many relationship with the Post model.
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()
    posts: Mapped[List["Post"]] = relationship("Post", back_populates="user")
    
    # Repr method for the User model.
    # Returns a string with the ID, username, and email of the user.
    def __repr__(self):
        return f"Id: {self.id}, Username: {self.username}, Email: {self.email}"
