import os
from celery_app import celery_app
from src.storage import sync_db
from src.models.space_image import SpaceImage
from PIL import Image
from sqlalchemy import select
from src.enums.enums import ImageStatus


@celery_app.task(bind=True, name="upload_image_task", max_retries=3)
def upload_image(self, temp_path: str, image_id: str):
    try:
        # open to validate image
        with Image.open(temp_path) as img:
            img.verify()

        print("Uploading...")

        url = f"https://circleground.ng/api/v1/space_image/{image_id}"

        with sync_db.get_session() as session:
            result = session.execute(
                select(SpaceImage).where(SpaceImage.id == image_id))
            space_image = result.scalars().first()
            if not space_image:
                return
            if space_image.status == ImageStatus.COMPLETED:
                return
            if space_image:
                space_image.url = url
                space_image.status = ImageStatus.COMPLETED

            session.commit()
            print("Success")

    except Exception as exc:
        with sync_db.get_session() as session:
            result = session.execute(
                select(SpaceImage).where(SpaceImage.id == image_id))
            space_image = result.scalars().first()
            if not space_image:
                return
            if space_image.status == ImageStatus.COMPLETED:
                return
            if space_image:
                space_image.status = ImageStatus.FAILED
                session.commit()
                print("Failed")

        raise self.retry(exc=exc, countdown=5)

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
