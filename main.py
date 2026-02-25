# import asyncio
# from fastapi import BackgroundTasks
# from src.services.super_admin_services import SuperAdminService
# from src.api.v1.dependencies import get_uow

from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.api.v1.routes.booking import booking_router
from src.api.v1.routes.auth import auth_router
from src.api.v1.routes.user import user_router
from src.api.v1.routes.space import space_router
from src.api.v1.routes.amenity import amenity_router
from src.api.v1.routes.space_amenities import space_amenities_router
from src.api.v1.routes.location import location_router
from src.api.v1.register_exceptions import register_exception_handlers
from src.core.pydantic_confirguration import config
from src.events.bootstrap import bootstrap_events_initializer
from src.storage import db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize event bus and subscriptions
    bootstrap_events_initializer()
    if config.DEV_ENV == 'development':
        await db.create_tables()
    yield
    # Cleanup actions can be added here if necessary
    await db.cleanup()

app = FastAPI(
    title="CircleGround App Backend",
    description="Backend API for Cirground App - Workspace listing solution",
    version="1.0.0",
    docs_url="/",
    redoc_url=None,
    lifespan=lifespan,

)

register_exception_handlers(app)


app.include_router(user_router)

app.include_router(space_router)

app.include_router(location_router)

app.include_router(auth_router)

app.include_router(space_amenities_router)

app.include_router(amenity_router)

app.include_router(booking_router)


# async def main():
#     background_tasks = BackgroundTasks()
#     async_session = db.session_maker()

#     async with get_uow(async_session) as uow:
#         service = SuperAdminService(uow)
#         super_admin = await service.create_first_super_admin(background_tasks)
#         print(super_admin)


# if __name__ == "__main__":
#     asyncio.run(main())
