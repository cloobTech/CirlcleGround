import asyncio
from src.storage import db

async def main():
    
    await db.drop_tables()
    print("Tables dropped")
    await db.create_table()
    print("Tables created")

if __name__ == "__main__":
    asyncio.run(main())