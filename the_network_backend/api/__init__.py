from fastapi import FastAPI
from .routes.Users import users_router

app = FastAPI()
app.include_router(users_router)
