from src.storage import sync_db
from src.models.user import User
from sqlalchemy import select


def try_sync():
    """Hello"""
    with sync_db.get_session() as session:
        result = session.execute(select(User))
        result = result.scalar_one()

        print(result)
        


#    result = session.execute(select(cls).filter(cls.id == obj_id))

try_sync()