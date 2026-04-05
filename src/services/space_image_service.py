from fastapi import UploadFile
from src.core.exceptions import EntityNotFound
from src.unit_of_work.unit_of_work import UnitOfWork


class SpaceImageService:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory

    async def create_space_image(self, space_id: str, files: list[UploadFile]):
        async with self.uow_factory as uow:
            image_records = []
            last_order = await uow.space_image_repo.get_last_order(space_id)
            for indx, file in enumerate(files):
                temp_path = f"/tmp/{file.filename}"
                with open(temp_path, "wb") as buffer:
                    buffer.write(file.file.read())
                    order = last_order + indx + 1
                image = await uow.space_image_repo.create(space_id=space_id, order=order)
                image_records.append((image, temp_path))
            return image_records

    async def delete_single_space_image(self, image_id: str):
        async with self.uow_factory as uow:
            
            await uow.space_image_repo.delete_single__space_image(image_id)
            return {
                "message": "Image deleted successfully",
            }

    async def delete_multiple_images(self, image_ids: list[str]):
        async with self.uow_factory as uow:
            await uow.space_image_repo.delete_multiple_images(image_ids)
            return {
                "message": "Images deleted successfully",
            }
