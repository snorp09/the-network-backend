from sqlalchemy.orm import Mapped, mapped_column
from .core import Base, SessionLocal

class User(Base):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column("username", str)
    email: Mapped[str] = mapped_column("email", str)
    password: Mapped[str] = mapped_column("password", str)