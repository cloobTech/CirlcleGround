from fastapi import FastAPI
from src.api.v1.routes.user_routes import user_router



app = FastAPI()

app.include_router(user_router) 