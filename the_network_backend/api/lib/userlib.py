from typing import Annotated
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from the_network_backend.settings import config_dict
from the_network_backend.api.models.user_models import User
from the_network_backend.db.models.User import User as DBUser
from the_network_backend.db.lib.userlib import get_user_by_email
import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

# Create JWT via PyJWT
async def create_jwt_token(data: dict, secret: str = config_dict["JWT_SECRET"], algorithm: str = "HS256"):
    """
    Creates a JWT token with the given data, secret, and algorithm.

    Parameters:
        data (dict): The data to encode in the token.
        secret (str): The secret key to sign the token.
        algorithm (str): The algorithm to use for signing the token.

    Returns:
        str: The encoded JWT token.
    """
    data.update({"exp": datetime.now(timezone.utc) + timedelta(minutes=15)})  # Set expiration time
    return jwt.encode(data, secret, algorithm=algorithm)

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    """
    Retrieves the current user from the JWT token.

    Parameters:
        token (str): The JWT token.

    Returns:
        dict: The decoded token data.
    """
    try:
        payload = jwt.decode(token, config_dict["JWT_SECRET"], algorithms=["HS256"])
        user = await get_user_by_email(payload["sub"])
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return User.model_validate(user)
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")