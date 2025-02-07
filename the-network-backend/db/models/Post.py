from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..core import Base

#Type checking imports
if TYPE_CHECKING:
    from .User import User

class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(foreign_key="users.id")

    user: Mapped["User"] = relationship("User", back_populates="posts")