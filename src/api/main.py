from fastapi import FastAPI
from src.api.v1.routes.user_routes import user_router
from src.api.v1.routes.space_routes import space_router



app = FastAPI()

app.include_router(user_router) 

app.include_router(space_router)