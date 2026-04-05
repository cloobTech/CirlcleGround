from src.storage import db
import asyncio

# from src.models.conversation import Conversation


# async def main(): 
#     new_conversation = Conversation()
#     print(new_conversation.id)
#     async with db.get_session() as session:
#         session.add(new_conversation)
#         await session.commit()
        
# asyncio.run(main())

from src.models import user, booking, space, location, space_addon, space_amenities, space_image, space_pricing, space_rule, space_use_case, amenities, custom_amenity, payments, reviews

async def main(): 
       
    try:
        await db.drop_tables()
        await db.create_tables()

    except ValueError as e:
        print(e)
        
asyncio.run(main())

