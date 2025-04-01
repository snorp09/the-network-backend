from fastapi import APIRouter
from ..models.user_models import User, UserIncoming
from the_network_backend.db.lib.userlib import create_user, get_user_by_email

users_router = APIRouter(prefix="/users", tags=["Users"])

@users_router.post("/create", response_model=User)
async def create_account(incoming_user: UserIncoming):
    user = await create_user(**incoming_user.model_dump())
    return User.model_validate(user)
