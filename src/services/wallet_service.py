import uuid
from sqlalchemy.exc import IntegrityError
from src.schemas.payment_schema import WithdrawalSchema
from src.unit_of_work.unit_of_work import UnitOfWork




class WalletService:
    def __init__(self, uow_factory: UnitOfWork):
        self.uow_factory = uow_factory

   