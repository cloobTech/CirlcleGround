from fastapi import APIRouter, Depends
from src.models.user import User
from src.api.v1.dependencies import get_current_user, get_bank_account_service
from src.schemas.bank_account_schema import CreateBankAccount
from src.services.bank_account_service import BankAccountService


bank_account_router = APIRouter(prefix="/api/v1/bank_accounts", tags=["Bank Accounts"])


@bank_account_router.post("/")
async def add_bank_account(
    account_details: CreateBankAccount,
    user: User = Depends(get_current_user),
    bank_account_service: BankAccountService = Depends(get_bank_account_service)
):
    response = await bank_account_service.add_bank_account(user_id=user.id, account_details=account_details)
    return response

