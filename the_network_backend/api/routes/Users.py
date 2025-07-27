from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from ..models.user_models import User, UserIncoming
from the_network_backend.db.lib.userlib import create_user, get_user_by_email, login_user as login_user_db
from the_network_backend.api.lib.userlib import create_jwt_token, get_current_user

users_router = APIRouter(prefix="/users", tags=["Users"])

@users_router.post("/create", response_model=User)
async def create_account(incoming_user: UserIncoming):
    """Create a new user account."""
    user = await create_user(**incoming_user.model_dump())
    return User.model_validate(user)

@users_router.post("/login")
async def login_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """Login a user and return a token."""
    user = await login_user_db(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = await create_jwt_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}


@users_router.get("/me", response_model=User)
async def get_me(current_user: Annotated[dict, Depends(get_current_user)]):
    """Get the current user."""
    return current_user
