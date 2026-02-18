from src.storage import db
import asyncio
from scripts.data import AMENITIES, REGISTER_USER, CREATE_SPACE, UPDATE_NEW_SPACE, SPACE_IMAGE
from src.models.amenities import Amenity
from src.models.user import User
from src.repositories.amenity_repo import AmenityRepository
from src.repositories.user_repo import UserRepository
from src.repositories.space_image_repo import SpaceImageRepository
from src.repositories.space_repo import SpaceRepository
from src.services.space_services import SpaceService
from src.unit_of_work.unit_of_work import UnitOfWork
from src.auth.security import hash_password
from src.schemas.space_schema import CreateSpaceSchema, UpdateSpaceAtCreation, SpaceImageSchema, SpaceSchema


async def seed_data():
    # Refresh the database
    await db.create_tables()

    async with db.get_session() as session:
        uow = UnitOfWork(session)
        space_service = SpaceService(uow)
        amenities = []
        for amenity in AMENITIES:
            amenities.append(Amenity(**amenity))
        amenity_repo = AmenityRepository(session)
        await amenity_repo.bulk_create(amenities)
        print(" =============================== Amenities created ===================================")

        user_repo = UserRepository(session)
        user = User(**REGISTER_USER)
        user.password = hash_password(user.password)
        await user_repo.create(user)
        print(" =============================== User created ===================================")

        space = SpaceSchema(**CREATE_SPACE)
        space_data = CreateSpaceSchema(space=space)
        new_space = await space_service.create_space(host_id=user.id, data=space_data)
        print(new_space)
        update_space = UpdateSpaceAtCreation(**UPDATE_NEW_SPACE)
        await space_service.update_new_space(space_id=new_space['id'], data=update_space)

        space_image_repo = SpaceImageRepository(session)
        for image in SPACE_IMAGE:
            await space_image_repo.create(space_id=new_space["id"], order=image["order"])

        # await space_repo.update(UPDATE_NEW_SPACE)
        # await space_repo.add_images(SPACE_IMAGE)
        print(" =============================== Space created ===================================")

        await session.commit()
        print(" =============================== Seeding completed ===================================")

        await db.cleanup()


if __name__ == "__main__":
    asyncio.run(seed_data())
