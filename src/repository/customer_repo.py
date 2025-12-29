from repository import base_repo
from sqlalchemy.ext.asyncio import AsyncSession
from models.customer import Customer

class CustomerRepository:
    async def save_customer(self, session: AsyncSession, obj):
        await base_repo.save(session, obj)
    
    async def get_all_customers(self, session: AsyncSession, cls):
        customers = await base_repo.get_by_class(session, Customer)
        return customers
    
    async def get_customer_by_id(self, session: AsyncSession, cls, object_id):
        customer = await base_repo.get_by_id(session, Customer, object_id)
        return customer
    
    async def update_customer_info(self, session: AsyncSession, cls, id, key, value):
        customer = await base_repo.update_info(session, Customer, id, key, value)
        return customer
    
    async def delete_customer_by_id(self, session: AsyncSession, cls, id):
        customer = await base_repo.delete_by_id(session, Customer, id)
        return None
    
    async def get_customer_by_email(self, session: AsyncSession, cls, email):
        customer = await base_repo.get_by_email(session, Customer, email)
        return customer