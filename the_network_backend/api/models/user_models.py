from pydantic import BaseModel, ConfigDict
from datetime import datetime

class UserIncoming(BaseModel):
    username: str
    email: str
    password: str

class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    email: str
    created_at: datetime